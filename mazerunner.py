import pygame
from pygame.locals import *
import time
from menu import startMenu, options, credit
from game import play

def principal():
    #Initialisation de la bibliothèque pygame
    pygame.init()

    #Creation de la fenetre
    screen = pygame.display.set_mode((1600, 900), FULLSCREEN)
    #screen = pygame.display.set_mode((800, 600), FULLSCREEN)
    #screen = pygame.display.set_mode((1440, 900), FULLSCREEN)

    #Fond noir
    screen.fill((0,0,0))


    difficulty = 1
    run = True
    while run:
        choice = startMenu(screen)
        if choice == 1:
            run = play(screen, difficulty)
            run = True
        elif choice == 2:
            res = options(screen)
            if res == False:
                run = False
            else:
                difficulty = res[0]
        elif choice == 3:
            run = False
    credit(screen)
    time.sleep(0.5)
    pygame.display.quit()

principal()
