import pygame
from pygame.locals import *

def startMenu(screen):
    #Impotation image menu
    fond = pygame.image.load("images/start.png").convert()
    screen.blit(fond, (0, 0))

    # Dessin du rectangle de selection
    x = 450
    y = 250
    pygame.draw.rect(screen, (200, 50, 50), (x, y, 650, 150), 5)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = True, stoppe si = False
    run = True

    #variables necessaire
    choice = 1
    # Boucle infinie
    while run:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
                choice = 3
            # Deplacement
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if choice > 1:
                        y -= 150
                        choice -= 1
                if event.key == K_DOWN:
                    if choice < 3:
                        y += 150
                        choice += 1
                if event.key == K_RETURN:
                    run = False
                # Re-collage
                screen.blit(fond, (0, 0))
                pygame.draw.rect(screen, (200, 50, 50), (x, y, 650, 150), 5)
                # Rafraichissement
                pygame.display.flip()
    return choice

def options(screen):
    fond = pygame.image.load("images/options.png").convert()
    screen.blit(fond, (0, 0))

    myfont = pygame.font.SysFont('Comic Sans MS', 72)
    tabText = ['FACILE', 'MOYEN', 'DIFFICILE']
    text = tabText[0]
    textsurface = myfont.render(text, False, (200, 50, 50))

    screen.blit(textsurface, (950, 220))

    # Dessin du rectangle de selection
    x = 30
    y = 200
    pygame.draw.rect(screen, (200, 50, 50), (x, y, 700, 150), 5)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = True, stoppe si = False
    run = True

    # variables necessaire
    choice = 1
    res = [1]

    # Boucle infinie
    while run:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
                res = False
            # Deplacement
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if choice > 1:
                        y -= 480
                        choice -= 1
                if event.key == K_DOWN:
                    if choice < 2:
                        y += 480
                        choice += 1
                if event.key == K_RIGHT:
                    if choice == 1:
                        if res[0] < 3:
                            res[0] += 1
                        else:
                            res[0] = 1
                if event.key == K_LEFT:
                    if choice == 1:
                        if res[0] > 1:
                            res[0] -= 1
                        else:
                            res[0] = 3
                if event.key == K_RETURN and choice == 2:
                    run = False

                text = tabText[res[0]-1]
                # Re-collage
                screen.blit(fond, (0, 0))
                textsurface = myfont.render(text, False, (200, 50, 50))
                pygame.draw.rect(screen, (200, 50, 50), (x, y, 700, 150), 5)
                screen.blit(textsurface, (950, 220))
                # Rafraichissement
                pygame.display.flip()
    return res

def credit(screen):
    fond = pygame.image.load("images/credits.png").convert()
    screen.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

def victoire_screen(screen):
    fond = pygame.image.load("images/victoire.png").convert()
    screen.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()