import pygame
from pygame.locals import *
from classPerso import Perso
from deplacements import mur
import time

def visible(map, cell, perso):
    i = cell[0]
    k = cell[1]
    x = perso.x
    y = perso.y
    tab = map.grid
    if tab[i][k].visitee == True or time.time() - tab[i][k].visitee < perso.memoire:
        return True

    else:
        if i == y - 1 and k == x:
            if not mur(x,y,'haut', map):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y and k == x + 1:
            if not mur(x,y,'droite', map):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y + 1 and k == x:
            if not mur(x,y,'bas', map):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y and k == x - 1:
            if not mur(x,y,'gauche', map):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True




        if i == y - 1 and k == x + 1:
            if (not mur(x,y,'haut', map) and not mur (x,y-1,'droite', map)) or (not mur(x,y,'droite', map) and not mur(x+1,y,'haut', map)):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y + 1 and k == x + 1:
            if (not mur(x,y,'bas', map) and not mur (x,y+1,'droite', map)) or (not mur(x,y,'droite', map) and not mur(x+1,y,'bas', map)):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y + 1 and k == x - 1:
            if (not mur(x,y,'bas', map) and not mur (x,y+1,'gauche', map)) or (not mur(x,y,'gauche', map) and not mur(x-1,y,'bas', map)):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
        if i == y - 1 and k == x - 1:
            if (not mur(x,y,'gauche', map) and not mur (x-1,y,'haut', map)) or (not mur(x,y,'haut', map) and not mur(x,y-1,'gauche', map)):
                if map.grid[i][k].visitee != True:
                    map.grid[i][k].visitee = time.time()
                return True
    return False