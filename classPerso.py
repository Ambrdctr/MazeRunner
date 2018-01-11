import pygame
from pygame.locals import *
import time
import random
from classChest import Bag
#objets qu'un perso (joueur ou marchand) peut poseder
from classObject import Epee, Couteau, Heaume, Cle, PotionVie, PotionForce, PotionVitesse, PotionMemoire

#Pour heritage
class Perso:
    
    def __init__(self, ici):
        """ici : un tuple (x, y) représentant un point dans l'espace"""
        self.x = ici[0] #position largeur
        self.y = ici[1] #position hauteur
        self.dir = 2 #direction (actualise lors des deplacements)

#le joueur (herite de la classe perso)
class Joueur(Perso):
    
    def __init__(self, ici, name, screen):
        """
        :param ici: position dans la grille
        :param name: nom (utile si on ajoute du multijoueur et eun classement general)
        :param screen: la fenetre d'affichage
        """

        Perso.__init__(self, ici) #heritage
        self.nom = name
        self.vivant = True #pour savoir lorsque le joueur est mort
        self.protection = 0 #utilise lors de l'equipement d'un casque
        self.vie = 100 #points de vie du joueur
        self.vitesse = 1 #vitesse d'attaque (1.5/vitesse)
        self.inventaire = Bag(screen) #objets possedes par le joueur (son sac a dos)
        self.force = 5 #sa force (degat infliges lors d'une attaque)
        self.memoire = 10 #temps pendant lequel il se souvient des cases qu'il a visite
        self.charisme = 0 #pour les achats et la revente, gain ou perte par rapport a l'operation en pourcent du prix de l'objet
        self.derniereAtt = False #pour pouvoir gerer la vitesse d'attaque sans affecter les deplacements
        #les images par rapport a la direction (0 = haut, 2= bas)
        self.images = [pygame.image.load("images/haut.png").convert_alpha(), pygame.image.load("images/droite.png").convert_alpha(),
                       pygame.image.load("images/bas.png").convert_alpha(), pygame.image.load("images/gauche.png").convert_alpha()]
        self.dansDonjon = False #pour tester des operations propres au donjon
        self.equipement = [False, False, False] #son equipement ([protection, potion, arme])

    def resetStats(self):
        """
        reinitialise les stats du perso lors de l'equipement d'un nouvel objet
        """
        self.protection = 0
        self.vitesse = 1
        self.force = 5
        self.memoire = 10

    def afficherEquipement(self, screen, id=False):
        """
        :param screen: affichage
        :param id: effet lors du survol
        :return: la position de toutes les cases du tableau sur l'ecran et la position du sac sur l'ecran
        """

        #dimensionnement par rapport a la taille de l'ecran
        tabAllObj = []
        size = screen.get_size()
        if size[0] <= size[1]:
            posx = (size[0] // 12) * 13
            taille_case = size[0] // 12
        else:
            posx = (size[1] // 12) * 13
            taille_case = size[1] // 12
        posy = (taille_case) * 8

        #rectangle du conteneur, utilise pour l'esuipement d'objet
        pygame.draw.rect(screen, (30, 30, 30), (posx, taille_case * 2, size[0] - posx, posy - taille_case * 2), 0)


        #image du joueur
        #----
        #collage et redimensionnement
        image = pygame.transform.scale(self.images[2], (int(taille_case * 1.5), int(taille_case * 2.5)))
        screen.blit(image, (posx + 5, taille_case * 4))
        #----

        #pour positionner plus facilement par rapport a l'image
        milieu = (posx + 5) + (int(taille_case * 1.5)) / 2
        gauche = int((milieu + (posx + 5)) / 2)
        droite = int((milieu + ((posx + 5) + (int(taille_case * 1.5)))) / 2)

        #protection
        #----
        pygame.draw.rect(screen, (220, 220, 220), (gauche, taille_case * 3 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + 1, taille_case * 3 + 11, droite - gauche - 1, droite - gauche - 1)
        #mouvmeent de la souris
        if id != False and id-1 == 0:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj) #ajout de la position de la case protection
        #----

        #potion
        #----
        pygame.draw.rect(screen, (220, 220, 220), (gauche, taille_case * 5 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + 1, taille_case * 5 + 11, droite - gauche - 1, droite - gauche - 1)
        if id != False and id-1 == 1:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj)
        #----

        #arme
        #----
        pygame.draw.rect(screen, (220, 220, 220), (gauche + taille_case + 10, taille_case * 5 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + taille_case + 11, taille_case * 5 + 11, droite - gauche - 1, droite - gauche - 1)
        if id != False and id-1 == 2:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj)
        #----

        #collage de l'image lors de l'equipement d'un objet
        if self.equipement[0] != False:
            image = pygame.transform.scale(self.equipement[0].image, (droite - gauche, droite - gauche))
            screen.blit(image, (tabAllObj[0][0], tabAllObj[0][1]))

        if self.equipement[1] != False:
            image = pygame.transform.scale(self.equipement[1].image, (droite - gauche, droite - gauche))
            screen.blit(image, (tabAllObj[1][0], tabAllObj[1][1]))

        if self.equipement[2] != False:
            image = pygame.transform.scale(self.equipement[2].image, (droite - gauche, droite - gauche))
            screen.blit(image, (tabAllObj[2][0], tabAllObj[2][1]))

        pygame.display.flip()

        #positions pour les operations au clic
        return (tabAllObj, Rect(gauche, taille_case * 3 + 10, taille_case + 11 + droite - gauche - 1, (taille_case * 2) + droite - gauche))

    def aCle(self):
        """
        :return: True si le joueur possede une cle
        """
        aCle = False
        for obj in self.inventaire.contenu:
            if isinstance(obj, Cle):
                aCle = True
                break
        return aCle

    def supprimerCle(self):
        """
        :return: supprime la premiere cle de l'inventaire du joueur
        """
        for obj in self.inventaire.contenu:
            if isinstance(obj, Cle):
                self.inventaire.contenu.remove(obj)
                index = self.inventaire.tabObj.index(obj)
                self.inventaire.tabObj[index] = False
                break



# un marchand
class Marchand():
    
    def __init__(self, name, screen):
        self.nom = name
        #possede un sac d'objet
        self.inventaire = Bag(screen)

        #remplissage du sac par rapport au nom du marchand
        if name == "Forgeron":
            listeObj = [Epee(screen), Couteau(screen), Heaume(screen), Cle(screen)]
            for i in range(len(listeObj)):
                self.inventaire.tabObj[i] = listeObj[i]
                self.inventaire.contenu.append(listeObj[i])

        elif name == "Sorciere":
            listeObj = [PotionVie(screen), PotionForce(screen), PotionVitesse(screen), PotionMemoire(screen)]
            for i in range(len(listeObj)):
                self.inventaire.tabObj[i] = listeObj[i]
                self.inventaire.contenu.append(listeObj[i])

#un monstre (herite de la classe perso car a une position
class Monstre(Perso):
    
    def __init__(self, ici, diff):
        Perso.__init__(self, ici)
        self.diff = diff
        self.vivant = True
        self.dansDonjon = True
        self.vie = 15+diff*5 #les monstres sont plus dur a battre par rapport a la difficulte
        self.dernierMvmt = time.time() #pour regler leur vitesse de deplacement
        self.vitesse = 1 / diff #temps entre chaque deplacement, contrairement au joueur ils attaquent a chaque deplacement
        self.dirRetour = 0 #pour les mouvements lorgiques
        self.force = random.randint(3, 3+diff*3)
        self.vision = diff*3 #nombre de cases maximale entre le joueur et le monstre pour que ce dernier le voit
        #image en fonction du deplacement
        self.images =  [pygame.image.load("images/m_haut.png").convert_alpha(), pygame.image.load("images/m_droite.png").convert_alpha(),
                       pygame.image.load("images/m_bas.png").convert_alpha(), pygame.image.load("images/m_gauche.png").convert_alpha()]

    def __str__(self):
        return str(self.vivant) + str(self.vie) + str(self.dernierMvmt)
