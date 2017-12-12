import pygame
from pygame.locals import *
from map import create_empty_map

def play(screen, difficulty):
    size = screen.get_size()
    map = create_empty_map(int(size[0]/50), int(size[1]/50))
    print(map)
