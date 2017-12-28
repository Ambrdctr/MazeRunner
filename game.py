import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause
from deplacements import deplacerPerso, deplacerMonstre
from classPerso import Perso, Joueur, Monstre
from fonctionCases import *
from labyrinthe import create_maze
import random
import time

def play(screen, difficulty):
    size = screen.get_size()

    out = True
    exterieur = create_empty_map(int(size[0] / 50), int(size[1] / 50))
    donjon = create_maze(30, 20, 10)

    map = exterieur

    perso = Joueur((3,1), 'Didier')

    liste_montres = []
    monstre = Monstre((5,3), difficulty)

    aBouge = False

    # Touche reste enfoncée
    pygame.key.set_repeat(100, 50)

    timestart = time.time()
    while out:
        affichage(screen, perso, monstre, map)
        # Rafraîchissement de l'écran
        pygame.display.flip()

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                out = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    out = not pause(screen)
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    aBouge = True
                    deplacerPerso(perso, map, monstre, event.key)
        if allerDonjon(map, perso):
            aBouge = False
            map = donjon
            perso.x = map.start[1]
            perso.y = map.start[0]
            perso.dansDonjon = True
        if aBouge:
            if allerExterieur(map, perso):
                perso.x = 0
                perso.y = 0
                map = exterieur
                perso.dansDonjon = False
        if victoire(map,perso):
            perso.x = 0
            perso.y = 0
            map = exterieur
            perso.dansDonjon = False

        if perso.dansDonjon:
            map.grid[perso.y][perso.x].visitee = time.time()
            if monstre.vivant:
                monstre.dernierMvmt = time.time()
                if monstre.dernierMvmt - timestart >= monstre.vitesse:
                    timestart = time.time()
                    monstre.dernierMvmt = time.time()
                    deplacerMonstre(monstre, map, perso)
    return out