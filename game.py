import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause
from Perso import Perso, Joueur

def play(screen, difficulty):
    size = screen.get_size()
    perso = Joueur((0,0), 'Player')
    out = True
    map = create_empty_map(int(size[0] / 50), int(size[1] / 50))
    while out:
        if affichage(screen, perso, map) == True:
            out = not pause(screen)

