import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause

def play(screen, difficulty):
    size = screen.get_size()
    map = create_empty_map(int(size[0]/50), int(size[1]/50))
    out = True
    while out:
        if affichage(screen,map) == True:
            out = not pause(screen)

