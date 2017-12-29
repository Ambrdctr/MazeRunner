import pygame
from pygame.locals import *
import random
import time

# Couleurs
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
darkBlue = (0, 0, 128)
white = (255, 255, 255)
black = (0, 0, 0)
pink = (255, 200, 200)

color_mur = black
color_porte = green
color_cle = green
cases1 = blue
cases2 = white

def afficher_map(screen, perso, monstres, map):
    # Fond
    taille_case = 100
    mer1 = pygame.image.load("images/eau1.png").convert()
    mer2 = pygame.image.load("images/eau2.png").convert()
    mer3 = pygame.image.load("images/eau3.png").convert()
    mer4 = pygame.image.load("images/eau4.png").convert()

    persoimg = perso.images[perso.dir]
    persoimg = pygame.transform.scale(persoimg, (int(taille_case/1.5), taille_case))

    mort = pygame.image.load("images/sang.png").convert_alpha()
    mort = pygame.transform.scale(mort, (taille_case, taille_case))


    x = perso.x
    y = perso.y
    tab = map.grid
    pos2 = 0

    for i in range((y - 3), (y + 5)):
        pos1 = 0
        for k in range((x - 6), (x + 7)):
            if i in range(0, len(tab)) and k in range(0, len(tab[i])):
                posx = taille_case * pos1
                posy = taille_case * pos2
                if perso.dansDonjon and time.time() - tab[i][k].visitee > perso.memoire:
                    case = pygame.image.load("images/ombre.png").convert()
                else:
                    case = pygame.image.load("images/" + tab[i][k].state + ".png").convert()
                case = pygame.transform.scale(case, (taille_case, taille_case))
                screen.blit(case, (posx, posy))
                    ##Si mur
                if tab[i][k].walls[0] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx, posy - 5, taille_case, 10), 0)
                if tab[i][k].walls[1] == True:
                    posx = taille_case * pos1 + taille_case
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx - 5, posy, 10, taille_case), 0)
                if tab[i][k].walls[2] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2 + taille_case
                    pygame.draw.rect(screen, color_mur, (posx, posy - 5, taille_case, 10), 0)
                if tab[i][k].walls[3] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx - 5, posy, 10, taille_case), 0)
            else:
                eau = random.randint(1,1)#, 4)
                posx = taille_case * pos1
                posy = taille_case * pos2
                if eau == 1:
                    screen.blit(mer1, (posx, posy))
                elif eau == 2:
                    screen.blit(mer2, (posx, posy))
                elif eau == 3:
                    screen.blit(mer3, (posx, posy))
                elif eau == 4:
                    screen.blit(mer4, (posx, posy))
            for monstre in monstres:
                monstreimg = monstre.images[monstre.dir]
                monstreimg = pygame.transform.scale(monstreimg, (taille_case, taille_case))
                if (k == monstre.x) and (i == monstre.y) and perso.dansDonjon:
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    if monstre.vivant:
                        screen.blit(monstreimg, (posx, posy))
                    else:
                        screen.blit(mort, (posx,posy))
            if (k == x) and (i == y) and perso.vivant:
                posx = taille_case * pos1 + int(taille_case/6)
                posy = taille_case * pos2
                screen.blit(persoimg, (posx, posy))
            pos1 += 1
        pos2 += 1

def afficherStats(screen, perso):
    pygame.draw.rect(screen, (0, 0, 0), (1300, 80, 300, 200), 0)
    myfont = pygame.font.SysFont('Comic Sans MS', 15)
    textsurface = myfont.render('Vie (' + str(perso.vie) + ')', False, (200, 200, 200))
    screen.blit(textsurface, (1320, 94))
    pygame.draw.rect(screen, (255,0,0), (1410, 100, perso.vie, 10), 0)
    textsurface = myfont.render('Vitesse (' + str(perso.vitesse) + ')', False, (200, 200, 200))
    screen.blit(textsurface, (1320, 114))
    pygame.draw.rect(screen, (0, 255, 0), (1410, 120, perso.vitesse*10, 10), 0)
    textsurface = myfont.render('Force (' + str(perso.force) + ')', False, (200, 200, 200))
    screen.blit(textsurface, (1320, 134))
    pygame.draw.rect(screen, (0, 0, 255), (1410, 140, perso.force, 10), 0)


def affichage(screen, perso, monstre, map):
    afficher_map(screen, perso, monstre, map)
    afficherStats(screen, perso)


def pause(screen):
    fond = pygame.image.load("images/pause.png").convert()
    screen.blit(fond, (0,0))
    # Rafraichissement
    pygame.display.flip()

    # Dessin du rectangle de selection
    x = 650
    y = 630
    pygame.draw.rect(screen, (200, 50, 50), (x, y, 320, 120), 5)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = True, stoppe si = False
    run = True

    # variables necessaire
    choice = False

    # Boucle infinie
    while run:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
                choice = True
            # Deplacement
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if not choice:
                        y -= 200
                        choice = True
                if event.key == K_DOWN:
                    if choice:
                        y += 200
                        choice = False
                if event.key == K_RETURN:
                    run = False

                # Re-collage
                screen.blit(fond, (0, 0))
                pygame.draw.rect(screen, (200, 50, 50), (x, y, 320, 120), 5)
                # Rafraichissement
                pygame.display.flip()
    return choice