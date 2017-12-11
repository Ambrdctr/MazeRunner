#Classe cellule
class Cell:
    """Classe définissant une cellule caractérisé par:
    -ses murs environnent : [top, right, bottom, left]
    -son etat : vide, entrée, sortie, porte
    -son ensemble
    """

    #Constructeur
    def __init__(self):
        self.walls = [False, False, False, False]
        self.state = 'gazon'

class Grid:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        grid = []
        for i in range(w):
            grid.append([])
            for j in range(h):
                # Ajout de l'indice pour le calcul des ensemble
                grid[i].append(Cell())
        self.grid = grid


def create_empty_map(w,h):
    return Grid(w,h)
