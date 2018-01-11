#Ambroise Decouttere
#Tournafond Raphael
#L2 CMI INFO


#Importation des bibliothèques
import pygame
from pygame.locals import * #variables
import time
from menu import startMenu, options, credit
from game import play

def principal(x, y, bool):
    """
    Programme principal
    :param x: largeur de la fenetre, entier
    :param y: hauteur de la fenetre, entier
    :param bool: booleen si oui ou non fenetre redimensionnable
    :return: /
    """

    #Initialisation de la bibliothèque pygame
    pygame.init()

    # Creation de la fenetre
    if bool:
        screen = pygame.display.set_mode((x, y), RESIZABLE) #Redimensionnable
    else:
        screen = pygame.display.set_mode((x, y), FULLSCREEN) #Plein ecran

    #screen = pygame.display.set_mode((1600, 900), FULLSCREEN)
    #screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
    #screen = pygame.display.set_mode((1366, 768), FULLSCREEN)
    #screen = pygame.display.set_mode((800, 600), RESIZABLE)
    #screen = pygame.display.set_mode((1440, 900), FULLSCREEN)

    #Fond noir
    screen.fill((0,0,0))


    difficulty = 1 #1 : Facile, 2: Moyen, 3: Difficile
    run = True
    #Boucle principale
    while run:
        choice = startMenu(screen) #Affichage du menu initial
        if choice == 1:
            play(screen, difficulty) #choix : jouer, lancement du jeu
        elif choice == 2: #choix option, lancement menu de(s) option(s)
            res = options(screen)
            if res == False: #Si dans les options l'utilisateur clique sur la croix, fermeture du jeu
                run = False
            else:
                difficulty = res[0] #La difficulté change est prends la valeur de celle choisie
        elif choice == 3: #choix : quitter, fermeture du programme principal
            run = False
    credit(screen) #affichage de l'ecran des crédits
    pygame.display.quit() #arrêt de l'affichage, fermeture de la fenetre

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