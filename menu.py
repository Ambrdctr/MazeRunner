import pygame
from pygame.locals import *
from convertisseur import convertirSecondes
import time

def startMenu(screen):
    size = screen.get_size()
    #Impotation image menu
    fond = pygame.image.load("images/start.png").convert()
    fond = pygame.transform.scale(fond,(size[0], size[1]))
    screen.blit(fond, (0, 0))

    # Dessin du rectangle de selection
    x = int(450*size[0]/1600)
    y = int(250*size[1]/900)
    pygame.draw.rect(screen, (200, 50, 50), (x, y, int(650*size[0]/1600), int(150*size[1]/900)), 5)

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
                        y -= int(150*size[1]/900)
                        choice -= 1
                if event.key == K_DOWN:
                    if choice < 3:
                        y += int(150*size[1]/900)
                        choice += 1
                if event.key == K_RETURN:
                    run = False
                # Re-collage
                screen.blit(fond, (0, 0))
                pygame.draw.rect(screen, (200, 50, 50), (x, y, int(650*size[0]/1600), int(150*size[1]/900)), 5)
                # Rafraichissement
                pygame.display.flip()
    return choice

def options(screen):
    size = screen.get_size()
    fond = pygame.image.load("images/options.png").convert()
    fond = pygame.transform.scale(fond, (size[0], size[1]))
    screen.blit(fond, (0, 0))

    myfont = pygame.font.SysFont('Comic Sans MS', int(65*size[1]/900))
    tabText = ['FACILE', 'MOYEN', 'DIFFICILE']
    text = tabText[0]
    textsurface = myfont.render(text, False, (200, 50, 50))

    screen.blit(textsurface, (int(950*size[0]/1600), int(220*size[1]/900)))

    # Dessin du rectangle de selection
    x = int(30*size[0]/1600)
    y = int(200*size[1]/900)
    pygame.draw.rect(screen, (200, 50, 50), (x, y, int(700*size[0]/1600), int(150*size[1]/900)), 5)

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
                        y -= int(480*size[1]/900)
                        choice -= 1
                if event.key == K_DOWN:
                    if choice < 2:
                        y += int(480*size[1]/900)
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
                pygame.draw.rect(screen, (200, 50, 50), (x, y, int(700*size[0]/1600), int(150*size[1]/900)), 5)
                screen.blit(textsurface, (int(950*size[0]/1600), int(220*size[1]/900)))
                # Rafraichissement
                pygame.display.flip()
    return res

def credit(screen):
    size = screen.get_size()
    fond = pygame.image.load("images/credits.png").convert()
    fond = pygame.transform.scale(fond, (size[0], size[1]))
    screen.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

<<<<<<< HEAD
def victoire_screen(screen, temps):
    size = screen.get_size()
    fond1 = pygame.image.load("images/victoire1.png").convert()
    fond1 = pygame.transform.scale(fond1, (size[0], size[1]))
=======
def victoire_screen(screen):
    size = screen.get_size()
    fond = pygame.image.load("images/victoire.png").convert()
    fond = pygame.transform.scale(fond, (size[0], size[1]))
    screen.blit(fond, (0, 0))
>>>>>>> Ambroise

    fond2 = pygame.image.load("images/victoire2.png").convert()
    fond2 = pygame.transform.scale(fond2, (size[0], size[1]))


    #Affichage du texte
    myfont = pygame.font.SysFont('Comic Sans MS', int(72 * size[1] / 900))
    text = convertirSecondes(round(temps,0))
    print(text)
    textsurface = myfont.render(text, False, (200, 50, 50))

    run = True
    affiche = time.time()

    # Boucle infinie
    while run:

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            # ou echap
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False
        if time.time()-affiche > 1:
            screen.blit(fond1, (0, 0))
            if time.time()-affiche > 1.3:
                affiche = time.time()
        else:
            screen.blit(fond2, (0, 0))
        screen.blit(textsurface, (int(500 * size[0] / 1600), int(500 * size[1] / 900)))
        # Rafraichissement
        pygame.display.flip()

def sortir(screen):
    size = screen.get_size()
    fond = pygame.image.load("images/sortir.png").convert()
    fond = pygame.transform.scale(fond, (size[0], size[1]))
    screen.blit(fond, (0, 0))

    # Dessin du rectangle de selection
    x = int(650*size[0]/1600)
    y = int(360*size[1]/900)
    pygame.draw.rect(screen, (200, 50, 50), (x, y, int(300*size[0]/1600), int(130*size[1]/900)), 5)

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = True, stoppe si = False
    run = True

    # variables necessaire
    res = True
    # Boucle infinie
    while run:
        # Limitation de vitesse de la boucle
        # 30 frames par secondes suffisent
        pygame.time.Clock().tick(30)

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            # Deplacement
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if not res:
                        y -= int(210*size[1]/900)
                        res = True
                if event.key == K_DOWN:
                    if res:
                        y += int(210*size[1]/900)
                        res = False
                if event.key == K_RETURN:
                    run = False
                # Re-collage
                screen.blit(fond, (0, 0))
                pygame.draw.rect(screen, (200, 50, 50), (x, y, int(300*size[0]/1600), int(130*size[1]/900)), 5)
                # Rafraichissement
                pygame.display.flip()
    return res