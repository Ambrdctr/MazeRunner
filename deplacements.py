import pygame
from pygame.locals import *
import random
from classPerso import Monstre
import math
import classChest
from echanges import echange


def mur(x,y,direction, map):
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

def ya_monstre(xPrec, yPrec, monstres, direction):
    res = False
    for m in monstres:
        if direction == 'haut':
            ySuiv = (yPrec - 1)
            xSuiv = xPrec
        if direction == 'droite':
            xSuiv = (xPrec + 1)
            ySuiv = yPrec
        if direction == 'bas':
            ySuiv = (yPrec + 1)
            xSuiv = xPrec
        if direction == 'gauche':
            xSuiv = (xPrec - 1)
            ySuiv = yPrec
        if m.x == xSuiv and m.y == ySuiv:
            res = True
            break
    return res



def attMonstre(x, y, direction, monstre, perso, map):
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
            monstre.vie += - random.randint(perso.force-2, perso.force+2)
            if monstre.vie <= 0:
                monstre.vivant = False
                res = False
    return res

def ya_coffre(x, y, direction, coffres, perso):
    res = False
    yPrec = y
    xPrec = x
    for coffre in coffres:
        if direction == 'haut':
            ySuiv = (y - 1)
            if yPrec != ySuiv and ySuiv == coffre.y and xPrec == coffre.x:
                res = True
        if direction == 'droite':
            xSuiv = (x + 1)
            if xPrec != xSuiv and xSuiv == coffre.x and yPrec == coffre.y:
                res = True
        if direction == 'bas':
            ySuiv = (y + 1)
            if yPrec != ySuiv and ySuiv == coffre.y and xPrec == coffre.x:
                res = True
        if direction == 'gauche':
            xSuiv = (x - 1)
            if xPrec != xSuiv and xSuiv == coffre.x and yPrec == coffre.y:
                res = True
        if res:
            echange(perso, coffre)
            break

    return res

def monstre_ya_coffre(x, y, direction, coffres):
    res = False
    yPrec = y
    xPrec = x
    for coffre in coffres:
        if direction == 'haut':
            ySuiv = (y - 1)
            if yPrec != ySuiv and ySuiv == coffre.y and xPrec == coffre.x:
                res = True
        if direction == 'droite':
            xSuiv = (x + 1)
            if xPrec != xSuiv and xSuiv == coffre.x and yPrec == coffre.y:
                res = True
        if direction == 'bas':
            ySuiv = (y + 1)
            if yPrec != ySuiv and ySuiv == coffre.y and xPrec == coffre.x:
                res = True
        if direction == 'gauche':
            xSuiv = (x - 1)
            if xPrec != xSuiv and xSuiv == coffre.x and yPrec == coffre.y:
                res = True
        if res:
            break

    return res

def attPerso(x, y, direction, perso, monstre, map):
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
            attaque =  random.randint(monstre.force - 2, monstre.force + 2)
            if perso.protection > 0:
                perso.protection -= attaque
                perso.equipement[0].protection -= attaque
            else:
                perso.protection = 0
                perso.vie -= attaque
            if perso.vie <= 0:
                perso.vivant = False
                res = False
    return res


def deplacerPerso(perso, map, monstres, coffres, key):

    res = False

    x = perso.x
    y = perso.y

    pas_monstre = True
    pas_coffre = True
    if key == K_UP:
        perso.dir = 0
        if y > 0 and not mur(x, y, 'haut', map):
            for monstre in monstres:
                if attMonstre(x, y, 'haut', monstre, perso, map):
                    pas_monstre = False
            if ya_coffre(x, y, 'haut', coffres, perso):
                pas_coffre = False
            if pas_monstre and pas_coffre:
                perso.y -= 1
                res = True
    if key == K_DOWN:
        perso.dir = 2
        if y < map.w-1 and not mur(x, y, 'bas', map):
            for monstre in monstres:
                if attMonstre(x, y, 'bas', monstre, perso, map):
                    pas_monstre = False
            if ya_coffre(x, y, 'bas', coffres, perso):
                pas_coffre = False
            if pas_monstre and pas_coffre:
                perso.y += 1
                res = True
    if key == K_RIGHT:
        perso.dir = 1
        if x < map.h-1 and not mur(x, y, 'droite', map):
            for monstre in monstres:
                if attMonstre(x, y, 'droite', monstre, perso, map):
                    pas_monstre = False
            if ya_coffre(x, y, 'droite', coffres, perso):
                pas_coffre = False
            if pas_monstre and pas_coffre:
                perso.x += 1
                res = True
    if key == K_LEFT:
        perso.dir = 3
        if x > 0 and not mur(x, y, 'gauche', map):
            for monstre in monstres:
                if attMonstre(x, y, 'gauche', monstre, perso, map):
                    pas_monstre = False
            if ya_coffre(x, y, 'gauche', coffres, perso):
                pas_coffre = False
            if pas_monstre and pas_coffre:
                perso.x -= 1
                res = True
    return res



def deplacerMonstre(monstre, monstres, coffres, map, perso):

    x = monstre.x
    y = monstre.y

    deplacementMonstre = [K_UP, K_DOWN, K_RIGHT, K_LEFT]
    passage = False
    passagePossible = []

    distance = math.sqrt(math.pow(perso.x - x, 2) + math.pow(perso.y - y, 2))
    peut_bouger = False

    #Depalcement logique lorsque la distance du perso est inférieur ou égale à la vision du monstre
    if distance <= monstre.vision and distance != 0 and (monstre.force >= perso.force or random.random() >= 0.8):
        if math.sqrt(math.pow(perso.x - x, 2)) > math.sqrt(math.pow(perso.y - y, 2)):
            if perso.x > x: key = K_RIGHT
            elif perso.x < x: key = K_LEFT
        elif math.sqrt(math.pow(perso.x - x, 2)) < math.sqrt(math.pow(perso.y - y, 2)):
            if perso.y > y: key = K_DOWN
            elif perso.y < y: key = K_UP
        else:
            if random.randint(1,2) == 1:
                if perso.x > x: key = K_RIGHT
                elif perso.x < x: key = K_LEFT
            else:
                if perso.y > y: key = K_DOWN
                elif perso.y < y: key = K_UP
        if key == K_UP:
            peut_bouger = not mur(x, y, 'haut', map) and not monstre_ya_coffre(x, y, 'haut', coffres) and y > 0
        if key == K_DOWN:
            peut_bouger = not mur(x, y, 'bas', map) and not monstre_ya_coffre(x, y, 'bas', coffres) and y < map.w - 1
        if key == K_LEFT:
            peut_bouger = not mur(x, y, 'gauche', map) and not monstre_ya_coffre(x, y, 'gauche', coffres) and x > 0
        if key == K_RIGHT:
            peut_bouger = not mur(x, y, 'droite', map) and not monstre_ya_coffre(x, y, 'droite', coffres) and x < map.h - 1
    if not peut_bouger:
        for elt in deplacementMonstre:
            if elt != monstre.dirRetour:
                if elt == K_UP and not mur(x, y, 'haut', map) and not monstre_ya_coffre(x, y, 'haut', coffres) and y > 0:
                    passage = True
                    passagePossible.append(elt)
                if elt == K_DOWN and not mur(x, y, 'bas', map) and not monstre_ya_coffre(x, y, 'bas', coffres) and y < map.w-1:
                    passage = True
                    passagePossible.append(elt)
                if elt == K_LEFT and not mur(x, y, 'gauche', map) and not monstre_ya_coffre(x, y, 'gauche', coffres) and x > 0:
                    passage = True
                    passagePossible.append(elt)
                if elt == K_RIGHT and not mur(x, y, 'droite', map) and not monstre_ya_coffre(x, y, 'droite', coffres) and x < map.h-1:
                    passage = True
                    passagePossible.append(elt)

        if passage == False:
            key = monstre.dirRetour
        else:
            key = random.choice(passagePossible)

    if key == K_UP :
        monstre.dir = 0
        monstre.dirRetour = K_DOWN
        if not attPerso(x, y, 'haut', perso, monstre, map) and not ya_monstre(x, y, monstres, 'haut'):
            monstre.y -= 1
    if key == K_DOWN :
        monstre.dir = 2
        monstre.dirRetour = K_UP
        if not attPerso(x, y, 'bas', perso, monstre, map) and not ya_monstre(x, y, monstres, 'bas'):
            monstre.y += 1
    if key == K_LEFT :
        monstre.dir = 3
        monstre.dirRetour = K_RIGHT
        if not attPerso(x, y, 'gauche', perso, monstre, map) and not ya_monstre(x, y, monstres, 'gauche'):
            monstre.x -= 1
    if key == K_RIGHT :
        monstre.dir = 1
        monstre.dirRetour = K_LEFT
        if not attPerso(x, y, 'droite', perso, monstre, map) and not ya_monstre(x, y, monstres, 'droite'):
            monstre.x += 1


