import pygame
from pygame.locals import *

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

def deplacerPerso(perso, map, key):

    x = perso.x
    y = perso.y

    if key == K_UP:
        perso.dir = 0
        if y > 0 and not mur(x, y, 'haut', map):
            perso.y -= 1

    if key == K_DOWN:
        perso.dir = 2
        if y < map.w-1 and not mur(x, y, 'bas', map):
            perso.y += 1

    if key == K_RIGHT:
        perso.dir = 1
        if x < map.h-1 and not mur(x, y, 'droite', map):
            perso.x += 1

    if key == K_LEFT:
        perso.dir = 3
        if x > 0 and not mur(x, y, 'gauche', map):
            perso.x -= 1