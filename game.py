import pygame
from pygame.locals import *
from map import create_empty_map

def play(screen):
    size = fenetre.get_size()
    map = create_empty_map(size[0], size[1])
