import pygame
from pygame.locals import *
import random

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
        Objet.__init__(self, 80, 0.05, "cle", screen)


class Couteau(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 0.8, "couteau", screen)
        self.force = 5

class Epee(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 50, 2, "epee", screen)
        self.force = 15

class Casque(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 1.5, "casque", screen)
        self.protection = 20

class Heaume(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 50, 3, "heaume", screen)
        self.protection = 50

class PotionVie(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 40, 6, "pt1", screen)
        self.vie = 20

class PotionForce(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 40, 6, "pt2", screen)
        self.force = 10
        self.temps = False
        self.duree = random.randint(30, 45)

class PotionVitesse(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt3", screen)
        self.vitesse = 5
        self.temps = False
        self.duree = random.randint(30, 45)

class PotionMemoire(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt4", screen)
        self.memoire = 30
        self.temps = False
        self.duree = random.randint(60, 80)
