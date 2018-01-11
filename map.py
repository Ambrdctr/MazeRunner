import random
#VOIR labyrinthe.py POUR PLUS DE DETAILS
#Classe cellule
class Cell:
    """Classe définissant une cellule caractérisé par:
    -ses murs environnent : [top, right, bottom, left]
    -son etat : vide, entrée, sortie, porte
    -son ensemble
    """

    #Constructeur
    def __init__(self):
        tabSols = ['gazon', 'gazon', 'gazon', 'gazon', 'gazon', 'gazon', 'gravier', 'terre']
        self.walls = [False, False, False, False]
        self.state = random.choice(tabSols)

    def __str__(self):
        return self.state

class Grid:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.liste_monstres = []
        self.liste_coffres = []
        grid = []
        cellInt = Cell()
        for i in range(w):
            grid.append([])
            for j in range(h):
                if i == 0:
                    cellInt.walls[0] = True
                if j == h-1:
                    cellInt.walls[1] = True
                if i == w-1:
                    cellInt.walls[2] = True
                if j == 0:
                    cellInt.walls[3] = True
                grid[i].append(cellInt)
                cellInt = Cell()
        self.grid = grid

    def __str__(self):
        ch = ""
        for i in range(self.w):
            for j in range(self.h):
                ch += self.grid[i][j].__str__() + " "
            ch += '\n'
        return ch


def create_empty_map():
    #postionnement d'element
    map = Grid(20,30)
    map.grid[2][3].state = 'entreeDonjon'
    map.grid[10][1].state = 'forgeron'
    map.grid[10][3].state = 'sorciere'
    map.grid[10][5].state = 'acheteur'
    map.grid[5][7].state = 'coffre'
    return map
