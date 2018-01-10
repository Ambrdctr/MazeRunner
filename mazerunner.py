import pygame
from pygame.locals import *
import time
from menu import startMenu, options, credit
from game import play

def principal(x, y, bool):
    #Initialisation de la bibliothèque pygame
    pygame.init()

    # Creation de la fenetre
    if bool:
        screen = pygame.display.set_mode((x, y), RESIZABLE)
    else:
        screen = pygame.display.set_mode((x, y), FULLSCREEN)

    #screen = pygame.display.set_mode((1600, 900), FULLSCREEN)
    #screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
    #screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
    #screen = pygame.display.set_mode((800, 600), RESIZABLE)
    #screen = pygame.display.set_mode((1440, 900), FULLSCREEN)

    #Fond noir
    screen.fill((0,0,0))


    difficulty = 1
    run = True
    while run:
        choice = startMenu(screen)
        if choice == 1:
            play(screen, difficulty)
        elif choice == 2:
            res = options(screen)
            if res == False:
                run = False
            else:
                difficulty = res[0]
        elif choice == 3:
            run = False
    credit(screen)
    pygame.display.quit()

def un():
    print("Bienvenue dans MazeRunner, veuillez choisir votre résolution : ")
    print("(exemple : 640x480, 800x600, 1280x720, 1440x900, 1600x900 (max))")
    x = input("Largeur : ")
    y = input("Hauteur : ")
    fenetre = input("Fenetre ? (o/n) : ")
    if fenetre == 'o':
        bool = True
    else:
        bool = False
    principal(int(x), int(y), bool)

def deux():
    principal(800, 600, True)

#Vous pouvez choisir le programme initial à lancer ici (commentez celui que vous ne voulez pas)

un()
#deux()