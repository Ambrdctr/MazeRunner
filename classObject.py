import pygame
from pygame.locals import *
import random

#Tous les objets du jeu

class Objet:
    def __init__(self, value, weight, nom, screen):
        self.nom = nom
        self.valeur = value
        self.poid = weight #inutilise pour l'instant
        self.image = pygame.image.load("images/" + nom + ".png").convert_alpha()

    #ecriture du nom lors des print
    def __str__(self):
        return self.nom

#monnaie du jeu
class Piece(Objet):
    def __init__(self, v, screen):
        # v = 1, 2, 5, 10 ou 50
        Objet.__init__(self, v, v, "piece"+str(v), screen)

#permet d'ouvrir les trappe et le tresor
class Cle(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 80, 0.05, "cle", screen)

#armes contre les monstres
#----
class Couteau(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 0.8, "couteau", screen)
        #puissance de l'attaque ajoutee
        self.force = 5

class Epee(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 50, 2, "epee", screen)
        self.force = 15
#----

#protections contre l'attaque des monstres
#----
class Casque(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 1.5, "casque", screen)
        #valeur de la protection apportee
        self.protection = 20

class Heaume(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 50, 3, "heaume", screen)
        self.protection = 50
#----


#potions aux effets differents
#----

#ajoute de la vie (pas plus de 100)
class PotionVie(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt1", screen)
        #valeur de la vie ajoutee
        self.vie = random.randint(15, 25)

#ajoute de la force
class PotionForce(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 40, 6, "pt2", screen)
        #valeur de la force ajoutee
        self.force = 10
        #temps auquel la potion a ete bu
        self.temps = False
        #duree de l'effet
        self.duree = random.randint(30, 45)

#accelere la vitesse d'attaque
class PotionVitesse(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 40, 6, "pt3", screen)
        #valeur de la vitesse (1.5/vitesse)
        self.vitesse = random.randint(3,5)
        self.temps = False
        self.duree = random.randint(30, 45)

#augmente la memoire
class PotionMemoire(Objet):
    def __init__(self, screen):
        Objet.__init__(self, 20, 6, "pt4", screen)
        #valeur de la memoire ajoutee
        self.memoire = random.randint(25, 35)
        self.temps = False
        self.duree = random.randint(60, 80)
#----