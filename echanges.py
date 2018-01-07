import pygame
from pygame.locals import *

def echange(perso, coffre):
    perso.inventaire.afficher_sac("Inventaire")
    coffre.afficher_contenu(800, 300, "Coffre")

    run = True
    while run:

        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False