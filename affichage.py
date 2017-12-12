import pygame
from pygame.locals import *

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


def afficherMap(screen, map):

    taille_case = 50
    grid = map.grid

    for i in range(0, map.w):
        for j in range(0, map.h):
            case = pygame.image.load("images/" + grid[i][j].state + ".png").convert()
            screen.blit(case, (i*taille_case, j*taille_case))
            if grid[i][j].walls[0] == True:  ##Si mur
                posx = taille_case * k
                posy = taille_case * i
                pygame.draw.rect(screen, color_mur, (posx, posy - 5, taille_case, 10), 0)
            if grid[i][j].walls[1] == True:
                posx = taille_case * k + taille_case
                posy = taille_case * i
                pygame.draw.rect(screen, color_mur, (posx - 5, posy, 10, taille_case), 0)
            if grid[i][j].walls[2] == True:
                posx = taille_case * k
                posy = taille_case * i + taille_case
                pygame.draw.rect(screen, color_mur, (posx, posy - 5, taille_case, 10), 0)
            if grid[i][j].walls[3] == True:
                posx = taille_case * k
                posy = taille_case * i
                pygame.draw.rect(screen, color_mur, (posx - 5, posy, 10, taille_case), 0)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = True, stoppe si = False
    run = True

    # Boucle infinie
    while run:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                pause = False
                run = False
            # Deplacement
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pause = True
                    run = False
                # Rafraichissement
                pygame.display.flip()
    return pause

def affichage(screen, map):
    res = afficherMap(screen, map)
    afficherPerso(screen, perso, map)
    return res

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