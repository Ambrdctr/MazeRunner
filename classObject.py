import pygame
from pygame.locals import *

class Objet:
    def __init__(self, value, weight, nom, screen):
        self.nom = nom
        self.valeur = value
        self.poid = weight
        self.image = pygame.image.load("images/" + nom + ".png").convert_alpha()

    def __str__(self):
        return self.nom

class Piece(Objet):
    def __init__(self, v, screen):
        Objet.__init__(self, v, v, "piece"+str(v), screen)

class Cle(Objet):
    def __init__(self, screen):
        """color : de la forme (r,g,b)"""
        Objet.__init__(self, 10, 0.05, "cle", screen)


class Couteau(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 10, "couteau", screen)
        self.force = 5

class Epee(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 50, 6, "epee", screen)
        self.force = 15

class PotionVie(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt1", screen)
        self.vie = 20

class PotionForce(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt2", screen)
        self.force = 10
        self.temps = 120

class PotionMemoire(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt3", screen)
        self.memoire = 30

class PotionVitesse(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt4", screen)
        self.vitesse = 5
