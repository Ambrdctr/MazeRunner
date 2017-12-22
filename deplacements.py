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


def attMonstre(x, y, direction, monstre, perso, map):
    taille_case = 100
    carte = map.grid
    res = False
    yPrec = y
    xPrec = x
    if monstre.vivant and perso.dansDonjon:
        if direction=='haut':
            ySuiv = (y - 1)
            if yPrec != ySuiv and ySuiv == monstre.y and xPrec == monstre.x:
                res = True
        if direction=='droite':
            xSuiv = (x + 1)
            if xPrec != xSuiv and xSuiv == monstre.x and yPrec == monstre.y:
                res = True
        if direction=='bas':
            ySuiv = (y + 1)
            if yPrec != ySuiv and ySuiv == monstre.y and xPrec == monstre.x:
                res = True
        if direction=='gauche':
            xSuiv = (x - 1)
            if xPrec != xSuiv and xSuiv == monstre.x and yPrec == monstre.y:
                res = True
        if res == True:
            monstre.vie += - perso.force
            if monstre.vie <= 0:
                monstre.vivant = False
                res = False
    return res


def attPerso(x, y, direction, perso, monstre, map):
    taille_case = 100
    carte = map.grid
    res = False
    yPrec = y
    xPrec = x
    if perso.vivant and monstre.dansDonjon:
        if direction=='haut':
            ySuiv = (y - 1)
            if yPrec != ySuiv and ySuiv == perso.y and xPrec == perso.x:
                res = True
        if direction=='droite':
            xSuiv = (x + 1)
            if xPrec != xSuiv and xSuiv == perso.x and yPrec == perso.y:
                res = True
        if direction=='bas':
            ySuiv = (y + 1)
            if yPrec != ySuiv and ySuiv == perso.y and xPrec == perso.x:
                res = True
        if direction=='gauche':
            xSuiv = (x - 1)
            if xPrec != xSuiv and xSuiv == perso.x and yPrec == perso.y:
                res = True
        if res == True:
            perso.vie += - monstre.force
            if perso.vie <= 0:
                perso.vivant = False
                res = False
    return res


def deplacerPerso(perso, map, monstre, key):

    x = perso.x
    y = perso.y

    if key == K_UP:
        perso.dir = 0
        if y > 0 and not mur(x, y, 'haut', map) and not attMonstre(x, y, 'haut', monstre, perso, map):
            perso.y -= 1
    if key == K_DOWN:
        perso.dir = 2
        if y < map.w-1 and not mur(x, y, 'bas', map) and not attMonstre(x, y, 'bas', monstre, perso, map):
            perso.y += 1
    if key == K_RIGHT:
        perso.dir = 1
        if x < map.h-1 and not mur(x, y, 'droite', map) and not attMonstre(x, y, 'droite', monstre, perso, map):
            perso.x += 1
    if key == K_LEFT:
        perso.dir = 3
        if x > 0 and not mur(x, y, 'gauche', map) and not attMonstre(x, y, 'gauche', monstre, perso, map):
            perso.x -= 1



def deplacerMonstre(monstre, map, perso):

    x = monstre.x
    y = monstre.y

    deplacementMonstre = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
    abouger = False
    passage = False
    passagePossible = []

    for elt in deplacementMonstre:
        if elt != monstre.dirRetour:
            if elt == K_UP and not mur(x, y, 'haut', map) and y > 0:
                passage = True
                passagePossible.append(elt)
            if elt == K_DOWN and not mur(x, y, 'bas', map) and y < map.w-1:
                passage = True
                passagePossible.append(elt)
            if elt == K_LEFT and not mur(x, y, 'gauche', map) and x > 0:
                passage = True
                passagePossible.append(elt)
            if elt == K_RIGHT and not mur(x, y, 'droite', map) and x < map.h-1:
                passage = True
                passagePossible.append(elt)

    if passage == False:
        key = monstre.dirRetour
    else:
        key = random.choice(passagePossible)

    if key == K_UP :
        monstre.dir = 0
        monstre.dirRetour = K_DOWN
        if not attPerso(x, y, 'haut', perso, monstre, map):
            monstre.y -= 1
    if key == K_DOWN :
        monstre.dir = 2
        monstre.dirRetour = K_UP
        if not attPerso(x, y, 'bas', perso, monstre, map):
            monstre.y += 1
    if key == K_LEFT :
        monstre.dir = 3
        monstre.dirRetour = K_RIGHT
        if not attPerso(x, y, 'gauche', perso, monstre, map):
            monstre.x -= 1
    if key == K_RIGHT :
        monstre.dir = 1
        monstre.dirRetour = K_LEFT
        if not attPerso(x, y, 'droite', perso, monstre, map):
            monstre.x += 1


