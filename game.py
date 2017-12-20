import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause
from classPerso import Perso, Joueur

def play(screen, difficulty):
    size = screen.get_size()
    perso = Joueur((0,0), 'Player')
    out = True
    map = create_empty_map(int(size[0] / 50), int(size[1] / 50))
    map.grid[2][3].state = 'entree'
    map.grid[10][1].state = 'forgeron'
    map.grid[10][3].state = 'sorciere'
    map.grid[10][5].state = 'acheteur'
    perso = pygame.image.load("images/bas.png").convert_alpha()
    while out:
        if affichage(screen, perso, map) == True:
            out = not pause(screen)
        else:
            out = False
    return out