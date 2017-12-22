import pygame
from pygame.locals import *
import time

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
        self.vivant = True
        self.vie = 100
        self.vitesse = 1
        self.force = 5
        self.memoire = 30
        self.charisme = 0
        #self.inventaire = Bag()
        self.images = [pygame.image.load("images/haut.png").convert_alpha(), pygame.image.load("images/droite.png").convert_alpha(),
                       pygame.image.load("images/bas.png").convert_alpha(), pygame.image.load("images/gauche.png").convert_alpha()]
        self.dansDonjon = False


class Marchand(Perso):
    
    def __init__(self, ici, name):
        Perso.__init__(self, ici)
        self.nom = name
        self.inventaire = Bag()
        
class Monstre(Perso):
    
    def __init__(self, ici, diff):
        Perso.__init__(self, ici)
        self.vivant = True
        self.dansDonjon = True
        self.vie = 10*diff
        self.dernierMvmt = 0
        self.vitesse = 3 / diff
        self.dirRetour = 0
        self.force = 5
        self.vision = 0
        self.images =  [pygame.image.load("images/m_haut.png").convert_alpha(), pygame.image.load("images/m_droite.png").convert_alpha(),
                       pygame.image.load("images/m_bas.png").convert_alpha(), pygame.image.load("images/m_gauche.png").convert_alpha()]
