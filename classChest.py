import pygame
from pygame.locals import *
import random
from classObject import *


def tableau_d_objets(screen):
    """
    :param screen: necessaire à l'affichage des objets
    :return: un tableau d'objets nombreux en fonction de leur rareté
    """

    #Objets legendaires
    tab = [Piece(50, screen), Casque(screen), Heaume(screen), Epee(screen),
            PotionForce(screen), PotionMemoire(screen), PotionVie(screen), PotionVitesse(screen)]

    #Objets avec + de chances d'apparaitre
    for i in range(8): #Objets communs
        tab.append(Piece(1, screen))
        tab.append(Piece(2, screen))
    for i in range(6): #Objets peu communs
        tab.append(Piece(5, screen))
    for i in range(4): #Objets rares
        tab.append(Piece(10, screen))
        tab.append(Casque(screen))
        tab.append(Couteau(screen))

    return tab


#Sac d'objets
class Bag:


    #Initialisation
    def __init__(self, screen):
        self.ecran = screen #affichage
        self.capacite = 10 #capacite du sac en nb d'objets
        self.contenu = [] #Contenu du sac
        self.tabObj = [] #position des objets dans le sac
        self.pieces = 0 #pieces dans le sac
        for i in range(self.capacite):
            self.tabObj.append(False) #au depart tous les rangements du sac sont vides

    def afficher_sac(self, nom, id=False):
        """
        :param nom: affichage du sac dans la fenetre
        :param id: sert pour l'affichage avec survol de la souris
        :return: la position de toutes les cases du tableau sur l'ecran et la position du sac sur l'ecran
        """

        tabAllObj = []

        screen = self.ecran

        size = screen.get_size()

        #Affichage par rapport à la taille de la fenetre

        if size[0] <= size[1]:
            min = size[0]
            taille_case = size[0] // 12
        else:
            min = size[1]
            taille_case = size[1] // 12

        posy = (taille_case) * 8
        taille_police = min * 15 // 900

        #Encadrement des cases, rectangle du conteneur utilise pour les echanges
        pygame.draw.rect(screen, (200, 200, 200), (0, posy, 5*taille_case+20, (self.capacite//5)*taille_case+40), 0)

        #Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', taille_police)
        if self.pieces > 1:
            ch = " pièces"
        else:
            ch = " pièce"
        textsurface = myfont.render(nom + ", " + str(self.pieces) + ch, False, (50, 50, 50))
        screen.blit(textsurface, (5, posy + 5))

        #positionnement de la premiere cellule
        posy -= taille_case-taille_police*2
        tx = 0

        #dessin des cases
        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                posy += taille_case
            rx = tx*taille_case
            pygame.draw.rect(screen, (220, 220, 220), (rx+4, posy+4, taille_case+1, taille_case+1), 4)

            #si case selectionnee
            if id != False:
                if id-1 == x:
                    pygame.draw.rect(screen, (200, 200, 200), (rx+5, posy+5, taille_case, taille_case), 0)
                else:
                    pygame.draw.rect(screen, (180, 180, 180), (rx + 5, posy + 5, taille_case, taille_case), 0)
            else:
                pygame.draw.rect(screen, (180, 180, 180), (rx + 5, posy + 5, taille_case, taille_case), 0)
            tabAllObj.append(Rect(rx+5, posy+5, taille_case, taille_case))
            tx += 1
            #si il y a un objet
            if self.tabObj[x] != False:
                #dessiner l'objet
                image = pygame.transform.scale(self.tabObj[x].image, (taille_case, taille_case))
                screen.blit(image, (rx + 5, posy + 5))
        pygame.display.flip()

        return (tabAllObj, Rect(0, (taille_case) * 8, 5*taille_case+20, ((self.capacite//5)*taille_case+40)))


    def afficher_stock(self, nom, id=False):
        """
        comme afficher sac mais pour les marchands
        """

        allposTab = []

        screen = self.ecran

        size = screen.get_size()

        if size[0] <= size[1]:
            min = size[0]
            taille_case = size[0] // 12
        else:
            min = size[1]
            taille_case = size[1] // 12

        posy = (taille_case) * 8
        posx = (taille_case) * 13
        taille_police = min * 15 // 900

        # Encadrement des cases
        pygame.draw.rect(screen, (200, 200, 200),
                         (posx, posy, -(5 * taille_case + 20), (self.capacite // 5) * taille_case + 40), 0)

        # Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', taille_police)
        #Uniquement pour l'acheteur
        if self.pieces > 1:
            ch = ", " + str(self.pieces) + " pièces"
        elif self.pieces == 1:
            ch = ", 1 pièce"
        else:
            ch = ""
        textsurface = myfont.render(nom + ch, False, (50, 50, 50))
        screen.blit(textsurface, (posx - (5 * taille_case + 20) + 5, posy + 5))
        posy -= taille_case - taille_police * 2
        tx = 0

        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                posy += taille_case
            rx = tx * taille_case
            x1 = rx + (posx - (5 * taille_case + 20)) + 4
            y1 = posy + 4
            x2 = taille_case
            y2 = taille_case
            pygame.draw.rect(screen, (220, 220, 220), (x1, y1, x2 + 1, y2 + 1), 4)
            if id != False:
                if id - 1 == x:
                    pygame.draw.rect(screen, (200, 200, 200), (x1 + 1, y1 + 1, x2, y2), 0)
                else:
                    pygame.draw.rect(screen, (180, 180, 180), (x1 + 1, y1 + 1, x2, y2), 0)
            else:
                pygame.draw.rect(screen, (180, 180, 180), (x1 + 1, y1 + 1, x2, y2), 0)
            allposTab.append(Rect(x1, y1, x2, y2))
            tx += 1
            if self.tabObj[x] != False:
                image = pygame.transform.scale(self.tabObj[x].image, (taille_case, taille_case))
                screen.blit(image, (x1 + 1, y1 + 1))
        pygame.display.flip()

        return (allposTab, Rect(posx - (5 * taille_case + 20), (taille_case) * 8, (5 * taille_case + 20),
                                ((self.capacite // 5) * taille_case + 40)))


#Coffre (sac d'objet special)
class Chest(Bag):

    def __init__(self, x, y, img, screen):
        Bag.__init__(self, screen)
        #position dans le donjon
        self.x = x
        self.y = y
        #image en fonction du mur contre lequel il est pose
        images = [pygame.image.load("images/c_haut.png").convert_alpha(), pygame.image.load("images/c_droite.png").convert_alpha(),
                 pygame.image.load("images/c_bas.png").convert_alpha(), pygame.image.load("images/c_gauche.png").convert_alpha()]
        self.image = images[img]
        #reinitialisation du tableau d'objets
        self.tabObj = []
        #entre 3 et capacite -3 objets, tableau de nombre entre 0 et capacite -1
        tabN = random.sample(range(0, self.capacite-1), random.randint(3, self.capacite-3))
        #Generation de tous les objets
        tabObjets = tableau_d_objets(screen)
        for i in range(self.capacite):
            #si le i est dans tabN (si il y a un objet dans la case i
            if i in tabN:
                #ajouter l'objet
                self.tabObj.append(random.choice(tabObjets))
                self.contenu.append(self.tabObj[len(self.tabObj)-1])
            else:
                #mettre aucun objet
                self.tabObj.append(False)

    def __str__(self):
        return str(self.x)+str(self.y)

    def afficher_contenu(self, nom, id=False):
        """
        afficher sac adapte (positionnement à droite)
        """

        allposTab = []

        screen = self.ecran

        size = screen.get_size()

        if size[0] <= size[1]:
            min = size[0]
            taille_case = size[0] // 12
        else:
            min = size[1]
            taille_case = size[1] // 12

        posy = (taille_case) * 8
        posx = (taille_case) * 13
        taille_police = min * 15 // 900

        #Encadrement des cases
        pygame.draw.rect(screen, (200, 200, 200), (posx, posy, -(5*taille_case+20), (self.capacite//5)*taille_case+40), 0)

        #Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', taille_police)
        textsurface = myfont.render(nom, False, (50, 50, 50))
        screen.blit(textsurface, (posx-(5*taille_case+20)+5, posy+5))
        posy -= taille_case - taille_police * 2
        tx = 0

        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                posy += taille_case
            rx = tx*taille_case
            x1 = rx+(posx-(5*taille_case+20))+4
            y1 = posy+4
            x2 = taille_case
            y2 = taille_case
            pygame.draw.rect(screen, (220, 220, 220), (x1, y1, x2+1, y2+1), 4)
            if id != False:
                if id-1 == x:
                    pygame.draw.rect(screen, (200, 200, 200), (x1+1, y1+1, x2, y2), 0)
                else:
                    pygame.draw.rect(screen, (180, 180, 180), (x1 + 1, y1 + 1, x2, y2), 0)
            else:
                pygame.draw.rect(screen, (180, 180, 180), (x1 + 1, y1 + 1, x2, y2), 0)
            allposTab.append(Rect(x1, y1, x2, y2))
            tx += 1
            if self.tabObj[x] != False:
                image = pygame.transform.scale(self.tabObj[x].image, (taille_case, taille_case))
                screen.blit(image, (x1+1, y1+1))
        pygame.display.flip()

        return (allposTab, Rect(posx-(5*taille_case+20), (taille_case) * 8, (5*taille_case+20), ((self.capacite//5)*taille_case+40)))