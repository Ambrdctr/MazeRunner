import pygame
from pygame.locals import *
import time
import random
from classChest import Bag
from classObject import Epee, Couteau, Heaume, Cle, PotionVie, PotionForce, PotionVitesse, PotionMemoire

class Perso:
    
    def __init__(self, ici):
        """ici : un tuple (x, y) représentant un point dans l'espace"""
        self.x = ici[0]
        self.y = ici[1]
        self.dir = 2

class Joueur(Perso):
    
    def __init__(self, ici, name, screen):
        Perso.__init__(self, ici)
        self.nom = name
        self.vivant = True
        self.protection = 0
        self.vie = 100
        self.vitesse = 1
        self.inventaire = Bag(screen)
        self.force = 5
<<<<<<< HEAD
        self.memoire = 30
=======
        self.memoire = 1
>>>>>>> Ambroise
        self.charisme = 0
        self.images = [pygame.image.load("images/haut.png").convert_alpha(), pygame.image.load("images/droite.png").convert_alpha(),
                       pygame.image.load("images/bas.png").convert_alpha(), pygame.image.load("images/gauche.png").convert_alpha()]
        self.dansDonjon = False
        self.equipement = [False, False, False]

    def resetStats(self):
        self.protection = 0
        self.vitesse = 1
        self.force = 5
        self.memoire = 30

    def afficherEquipement(self, screen, id=False):

        tabAllObj = []
        size = screen.get_size()
        if size[0] <= size[1]:
            posx = (size[0] // 12) * 13
            taille_case = size[0] // 12
        else:
            posx = (size[1] // 12) * 13
            taille_case = size[1] // 12
        posy = (taille_case) * 8
        # taille_police = min * 15 // 900

        pygame.draw.rect(screen, (30, 30, 30), (posx, taille_case * 2, size[0] - posx, posy - taille_case * 2), 0)

        image = pygame.transform.scale(self.images[2], (int(taille_case * 1.5), int(taille_case * 2.5)))
        screen.blit(image, (posx + 5, taille_case * 4))

        milieu = (posx + 5) + (int(taille_case * 1.5)) / 2
        gauche = int((milieu + (posx + 5)) / 2)
        droite = int((milieu + ((posx + 5) + (int(taille_case * 1.5)))) / 2)


        pygame.draw.rect(screen, (220, 220, 220), (gauche, taille_case * 3 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + 1, taille_case * 3 + 11, droite - gauche - 1, droite - gauche - 1)

        if id != False and id-1 == 0:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj)

        pygame.draw.rect(screen, (220, 220, 220), (gauche, taille_case * 5 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + 1, taille_case * 5 + 11, droite - gauche - 1, droite - gauche - 1)
        if id != False and id-1 == 1:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj)

        pygame.draw.rect(screen, (220, 220, 220), (gauche + taille_case + 10, taille_case * 5 + 10, droite - gauche, droite - gauche), 4)
        rectObj = Rect(gauche + taille_case + 11, taille_case * 5 + 11, droite - gauche - 1, droite - gauche - 1)
        if id != False and id-1 == 2:
            pygame.draw.rect(screen, (200, 200, 200), rectObj, 0)
        else:
            pygame.draw.rect(screen, (180, 180, 180), rectObj, 0)

        tabAllObj.append(rectObj)

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

        return (tabAllObj, Rect(gauche, taille_case * 3 + 10, taille_case + 11 + droite - gauche - 1, (taille_case * 2) + droite - gauche))





class Marchand():
    
    def __init__(self, name, screen):
        self.nom = name
        self.inventaire = Bag(screen)

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

        
class Monstre(Perso):
    
    def __init__(self, ici, diff):
        Perso.__init__(self, ici)
        self.diff = diff
        self.vivant = True
        self.dansDonjon = True
        self.vie = 10*diff
        self.dernierMvmt = time.time()
        self.vitesse = 1 / diff
        self.dirRetour = 0
        self.force = random.randint(diff*3,diff*3+5)
        self.vision = diff*3
        self.images =  [pygame.image.load("images/m_haut.png").convert_alpha(), pygame.image.load("images/m_droite.png").convert_alpha(),
                       pygame.image.load("images/m_bas.png").convert_alpha(), pygame.image.load("images/m_gauche.png").convert_alpha()]

    def __str__(self):
        return str(self.vivant) + str(self.vie) + str(self.dernierMvmt)
