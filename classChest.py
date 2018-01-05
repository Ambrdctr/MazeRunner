import pygame
from pygame.locals import *
import random
from classObject import *


def tableau_d_objets(screen):
    tab = [Piece(50, screen), Cle(screen), Epee(screen),
            PotionForce(screen), PotionMemoire(screen), PotionVie(screen), PotionVitesse(screen)]

    #Objets avec + de chances d'apparaitre
    for i in range(5):
        tab.append(Piece(1, screen))
        tab.append(Piece(2, screen))
    for i in range(3):
        tab.append(Piece(5, screen))
    for i in range(2):
        tab.append(Piece(10, screen))
        tab.append(Couteau(screen))

    return tab


class Bag:

    def __init__(self, screen):
        self.ecran = screen
        self.capacite = 10
        self.contenu = []

    def afficher_sac(self, px, py, nom):

        # Opacité de l'arrière plan
        s = pygame.Surface((1600, 900))
        s.set_alpha(200)
        s.fill((0,0,0))
        self.ecran.blit(s, (0, 0))

        #Encadrement des cases
        taille_case = 100
        pygame.draw.rect(self.ecran, (200, 200, 200), (px-10, py+70, 5*taille_case+20, (self.capacite//5)*taille_case+40), 0)

        #Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(nom, False, (50, 50, 50))
        self.ecran.blit(textsurface, (px+5, py+73))
        y = py
        tx = 0

        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                y += taille_case
            rx = tx*taille_case+(px)
            pygame.draw.rect(self.ecran, (220, 220, 220), (rx-1, y-1, taille_case+1, taille_case+1), 4)
            pygame.draw.rect(self.ecran, (180, 180, 180), (rx, y, taille_case, taille_case), 0)
            tx += 1
            if x <= len(self.contenu)-1:
                self.ecran.blit(self.contenu[x].image, (rx, y))


class Chest(Bag):

    def __init__(self, x, y, img, screen):
        Bag.__init__(self, screen)
        self.x = x
        self.y = y
        images = [pygame.image.load("images/c_haut.png").convert_alpha(), pygame.image.load("images/c_droite.png").convert_alpha(),
                 pygame.image.load("images/c_bas.png").convert_alpha(), pygame.image.load("images/c_gauche.png").convert_alpha()]
        self.image = images[img]
        tabN = random.sample(range(0, self.capacite-1), random.randint(2, self.capacite-2))
        self.tabObj = []
        tabObjets = tableau_d_objets(screen)
        for i in range(self.capacite):
            if i in tabN:
                self.tabObj.append(random.choice(tabObjets))
                self.contenu.append(self.tabObj[len(self.tabObj)-1])
            else:
                self.tabObj.append(False)

    def __str__(self):
        return str(self.x)+str(self.y)

    def afficher_contenu(self, px, py, nom):

        #Encadrement des cases
        taille_case = 100
        pygame.draw.rect(self.ecran, (200, 200, 200), (px-10, py+70, 5*taille_case+20, (self.capacite//5)*taille_case+40), 0)

        #Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', 20)
        textsurface = myfont.render(nom, False, (50, 50, 50))
        self.ecran.blit(textsurface, (px+5, py+73))
        y = py
        tx = 0

        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                y += taille_case
            rx = tx*taille_case+(px)
            pygame.draw.rect(self.ecran, (220, 220, 220), (rx-1, y-1, taille_case+1, taille_case+1), 4)
            pygame.draw.rect(self.ecran, (180, 180, 180), (rx, y, taille_case, taille_case), 0)
            tx += 1
            if self.tabObj[x] != False:
                self.ecran.blit(self.tabObj[x].image, (rx, y))
        pygame.display.flip()