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

    def afficher_sac(self, nom):

        screen = self.ecran

        size = screen.get_size()

        if size[0] <= size[1]:
            min = size[0]
            taille_case = size[0] // 12
            posy = (taille_case) * 8
            posx = (taille_case) * 13
        else:
            min = size[1]
            taille_case = size[1] // 12
            posy = (taille_case) * 8
            posx = (taille_case) * 13
        taille_police = min * 15 // 900

        # Opacité de l'arrière plan
        s = pygame.Surface((1600, 900))
        s.set_alpha(200)
        s.fill((0,0,0))
        screen.blit(s, (0, 0))

        #pygame.draw.rect(screen, (20, 20, 20), (0, posy, posx // 2, size[1] - posy), 0)

        #Encadrement des cases
        pygame.draw.rect(screen, (200, 200, 200), (0, posy, 5*taille_case+20, (self.capacite//5)*taille_case+40), 0)

        #Ecriture du nom du contenant
        myfont = pygame.font.SysFont('Comic Sans MS', taille_police)
        textsurface = myfont.render(nom, False, (50, 50, 50))
        screen.blit(textsurface, (5, posy + 5))
        posy -= taille_case-taille_police*2
        tx = 0

        for x in range(0, self.capacite):
            if x % 5 == 0:
                tx = 0
                posy += taille_case
            rx = tx*taille_case
            pygame.draw.rect(screen, (220, 220, 220), (rx+4, posy+4, taille_case+1, taille_case+1), 4)
            pygame.draw.rect(screen, (180, 180, 180), (rx+5, posy+5, taille_case, taille_case), 0)
            tx += 1
            if x <= len(self.contenu)-1:
                screen.blit(self.contenu[x].image, (rx, posy))
        pygame.display.flip()


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

        screen = self.ecran

        size = screen.get_size()

        if size[0] <= size[1]:
            min = size[0]
            taille_case = size[0] // 12
            posy = (taille_case) * 8
            posx = (taille_case) * 13
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
            pygame.draw.rect(screen, (220, 220, 220), (rx+(posx-(5*taille_case+20))+4, posy+4, taille_case+1, taille_case+1), 4)
            pygame.draw.rect(screen, (180, 180, 180), (rx+(posx-(5*taille_case+20))+5, posy+5, taille_case, taille_case), 0)
            tx += 1
            if self.tabObj[x] != False:
                image = pygame.transform.scale(self.tabObj[x].image, (taille_case, taille_case))
                screen.blit(image, (rx+(posx-(5*taille_case+20)), posy))
        pygame.display.flip()