import pygame
from pygame.locals import *

def startMenu():
    #Initialisation de la bibliothèque pygame
    pygame.init()

    #Creation de la fenetre
    fenetre = pygame.display.set_mode((640, 480), FULLSCREEN)

    #Impotation image menu
    fond = pygame.image.load("start").convert()
    fenetre.blit(fond, (0, 0))

    # Rafraîchissement de l'écran
    pygame.display.flip()

    # Variable qui continue la boucle si = 1, stoppe si = 0
    continuer = 1

    # Boucle infinie
    while continuer:
        continue

startMenu()