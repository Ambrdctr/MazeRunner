import pygame
from pygame.locals import *

class Chest:

    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.size = 10
        self.contenu = []
        images = [pygame.image.load("images/c_haut.png").convert_alpha(), pygame.image.load("images/c_droite.png").convert_alpha(),
                 pygame.image.load("images/c_bas.png").convert_alpha(), pygame.image.load("images/c_gauche.png").convert_alpha()]
        self.image = images[img]

    def __str__(self):
        return str(self.x)+str(self.y)
