import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause
from deplacements import deplacerPerso
from classPerso import Perso, Joueur
from fonctionCases import *
from labyrinthe import create_maze

def play(screen, difficulty):
    size = screen.get_size()
    perso = Joueur((0,0), 'Player')
    out = True
    exterieur = create_empty_map(int(size[0] / 50), int(size[1] / 50))
    exterieur.grid[2][3].state = 'entree'
    exterieur.grid[10][1].state = 'forgeron'
    exterieur.grid[10][3].state = 'sorciere'
    exterieur.grid[10][5].state = 'acheteur'
    donjon = create_maze(10, 20)

    map = exterieur

    perso = Joueur((3,1), 'Didier')

    aBouge = False

    # Touche reste enfoncée
    pygame.key.set_repeat(100, 50)
    while out:
        affichage(screen, perso, map)
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
                    deplacerPerso(perso, map, event.key)
        if allerDonjon(map, perso):
            aBouge = False
            perso.x = 0
            perso.y = 0
            map = donjon
        if aBouge:
            if allerExterieur(map, perso):
                perso.x = 0
                perso.y = 0
                map = exterieur
    return out