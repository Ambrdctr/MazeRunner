import pygame
from pygame.locals import *

class Perso:
    
    def __init__(self, ici):
        """ici : un tuple (x, y) représentant un point dans l'espace"""
        self.x = ici[0]
        self.y = ici[1]
        self.dir = 2

class Joueur(Perso):
    
    def __init__(self, ici, name):
        Perso.__init__(self, ici)
        self.nom = name
        self.vie = 100
        self.vitesse = 1
        self.force = 5
        self.memoire = 30
        self.charisme = 0
        #self.inventaire = Bag()
        self.images = [pygame.image.load("images/haut.png").convert_alpha(), pygame.image.load("images/droite.png").convert_alpha(),
                       pygame.image.load("images/bas.png").convert_alpha(), pygame.image.load("images/gauche.png").convert_alpha()]

class Marchand(Perso):
    
    def __init__(self, ici, name):
        Perso.__init__(self, ici)
        self.nom = name
        self.inventaire = Bag()
        
class Monstre(Perso):
    
    def __init__(self, ici, pv, speed, strength, view):
        Perso.__init__(self, ici)
        self.vie = pv
        self.vitesse = speed
        self.force = strength
        self.vision = view
        self.inventaire = Bag()
        self.images = ['m_haut', 'm_droite', 'm_bas', 'm_gauche']

