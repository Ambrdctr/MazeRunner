import random
#Classe cellule
class Cell:
    """Classe définissant une cellule caractérisé par:
    -ses murs environnent : [top, right, bottom, left]
    -son etat : vide, entrée, sortie, porte
    -son ensemble
    """

    #Constructeur
    def __init__(self):
        tabSols = ['gazon', 'gravier', 'terre']
        self.walls = [False, False, False, False]
        self.state = random.choice(tabSols)

    def __str__(self):
        return self.state

class Grid:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        grid = []
        for i in range(w):
            grid.append([])
            for j in range(h):
                grid[i].append(Cell())
        self.grid = grid

    def __str__(self):
        ch = ""
        for i in range(self.w):
            for j in range(self.h):
                ch += self.grid[i][j].__str__() + " "
            ch += '\n'
        return ch


def create_empty_map(w,h):
    map = Grid(w,h)
    for i in range (1,map.w-1):
        map.grid[i][0].walls = [True, False, False, False]
        map.grid[i][map.h-1].walls = [False, False, True, False]
    return Grid(w,h)
