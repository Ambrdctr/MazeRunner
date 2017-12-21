import pygame
from pygame.locals import *
import random
from classPerso import Monstre


def mur(x,y,direction, map):
    taille_case = 100
    carte = map.grid
    res = False
    yPrec = y
    xPrec = x
    if direction=='haut':
        ySuiv = (y - 1)
        if yPrec != ySuiv and carte[yPrec][xPrec].walls[0]==True:
            res = True
    if direction=='droite':
        xSuiv = (x + 1)
        if xPrec != xSuiv and carte[yPrec][xPrec].walls[1]==True:
            res = True
    if direction=='bas':
        ySuiv = (y + 1)
        if yPrec != ySuiv and carte[yPrec][xPrec].walls[2]==True:
            res = True
    if direction=='gauche':
        xSuiv = (x - 1)
        if xPrec != xSuiv and carte[yPrec][xPrec].walls[3]==True:
            res = True
    return res


def attEnnemi(x,y,direction, ennemi, perso, map):
    taille_case = 100
    carte = map.grid
    res = False
    yPrec = y
    xPrec = x
    if ennemi.vivant and perso.dansDonjon:
        if direction=='haut':
            ySuiv = (y - 1)
            if yPrec != ySuiv and ySuiv == ennemi.y and xPrec == ennemi.x:
                res = True
        if direction=='droite':
            xSuiv = (x + 1)
            if xPrec != xSuiv and xSuiv == ennemi.x and yPrec == ennemi.y:
                res = True
        if direction=='bas':
            ySuiv = (y + 1)
            if yPrec != ySuiv and ySuiv == ennemi.y and xPrec == ennemi.x:
                res = True
        if direction=='gauche':
            xSuiv = (x - 1)
            if xPrec != xSuiv and xSuiv == ennemi.x and yPrec == ennemi.y:
                res = True
        if res == True:
            ennemi.vie += - perso.force
            if ennemi.vie <= 0:
                ennemi.vivant = False
                res = False
    return res

def deplacerPerso(perso, map, ennemi, key):

    x = perso.x
    y = perso.y

    if isinstance(perso, Monstre):
        deplacementMonstre = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
        abouger = False
        while not abouger:
            key = random.choice(deplacementMonstre)
            if key == K_UP and not mur(x, y, 'haut', map):
                abouger = True
            if key == K_DOWN and not mur(x, y, 'bas', map):
                abouger = True
            if key == K_LEFT and not mur(x, y, 'gauche', map):
                abouger = True
            if key == K_RIGHT and not mur(x, y, 'droite', map):
                abouger = True
    if key == K_UP:
        perso.dir = 0
        if y > 0 and not mur(x, y, 'haut', map) and not attEnnemi(x, y, 'haut', ennemi, perso, map):
            perso.y -= 1

    if key == K_DOWN:
        perso.dir = 2
        if y < map.w-1 and not mur(x, y, 'bas', map) and not attEnnemi(x, y, 'bas', ennemi, perso, map):
            perso.y += 1

    if key == K_RIGHT:
        perso.dir = 1
        if x < map.h-1 and not mur(x, y, 'droite', map) and not attEnnemi(x, y, 'droite', ennemi, perso, map):
            perso.x += 1

    if key == K_LEFT:
        perso.dir = 3
        if x > 0 and not mur(x, y, 'gauche', map) and not attEnnemi(x, y, 'gauche', ennemi, perso, map):
            perso.x -= 1


