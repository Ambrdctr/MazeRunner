from random import *
import time

class Cell:
    # Constructor
    def __init__(self, i):
        self.walls = [True, True, True, True]
        self.state = 'pierre'
        self.set = i
        self.visitee = False


class Room:
    # Constructor
    def __init__(self, x1, y1, x2, y2):
        self.left = y1
        self.right = y2 - 1
        self.top = x1
        self.bottom = x2 - 1
        self.visitee = False
        self.coffre = False

    def __str__(self):
        return "(" + str(self.left) + "," + str(self.top) + "), (" + str(self.right) + "," + str(self.bottom) + ")"

    def coord_border(self, grid):
        """
        :param grid: grille de cellule
        :return: un tableau de coordonnees correspondant a un bord de la piece et un entier pour savoir quel bord
        """
        res = False
        while not res:
            top = (self.top, randint(self.left+1, self.right-1))
            right = (randint(self.top+1, self.bottom-1), self.right)
            bottom = (self.bottom, randint(self.left+1, self.right-1))
            left = (randint(self.top+1, self.bottom-1), self.left)
            tab = [top, right, bottom, left]
            n = randint(0, 3)
            res = grid[tab[n][0]][tab[n][1]].walls[n]
        return (tab[n], n)

    def visite_cellules_piece(self, grid):
        """
        passe a true le parametre visitee de chaque cellule dans la piece
        """
        for i in range(self.left, self.right+1):
            for j in range(self.top, self.bottom+1):
                grid[j][i].visitee = True

    def renvoi_diff_coords(self, diff):
        #renvoi des coordonnees aleatoires de la piece
        coords = []
        for i in range(diff+1):
            coords.append((randint(self.left, self.right-1), randint(self.top, self.bottom-1)))
        return coords


class Grid:
    #carte du jeu
    def __init__(self, w, h, tresor):
        self.w = w #largeur
        self.h = h #hauteur
        randList = [(0, 0), (0, self.h - 1), (self.w - 1, self.h - 1), (self.w - 1, 0)]
        self.start = choice(randList) #choix d'un angle pour l'entree
        randList.remove(self.start)
        self.end = choice(randList) #choix d'un autre angle pour la sortie
        #initialisation des pieces monstres et coffres
        self.rooms = []
        self.liste_monstres = []
        self.liste_coffres = []
        grid = []
        ind = 0
        for i in range(w):
            grid.append([])
            for j in range(h):
                # Ajout de l'indice pour le calcul des ensemble
                initial_cell = Cell(ind)
                grid[i].append(initial_cell)
                ind += 1
        grid[self.start[0]][self.start[1]].state = 'entree'
        if tresor:
            grid[self.end[0]][self.end[1]].state = 'tresor'
        else:
            grid[self.end[0]][self.end[1]].state = 'trappe'
        #grille composee de cellules avec certaines d'etat special
        self.grid = grid

    def non_overlap_room(self, roomB):
        """
        :param roomB: piece a tester
        :return: renvoi true si la piece n'en overlap pas une autre
        """
        for roomA in self.rooms:
            if not (roomB.left      >   roomA.right   or
                    roomB.right     <   roomA.left    or
                    roomB.top       >   roomA.bottom  or
                    roomB.bottom    <   roomA.top     ):
                return False
        return True

    def est_dans_piece(self, cell):
        """
        :param cell: cellule a tester
        :return: true si la cellule est dans une piece
        """
        for roomA in self.rooms:
            if (roomA.left      <=   cell[0]     and
                roomA.right     >=   cell[0]     and
                roomA.top       <=   cell[1]     and
                roomA.bottom    >=   cell[1]     ):
                return roomA
        return False

    def have_neighbor(self, c, wall):
        #teste si une cellule a une cellule voisine
        if wall == 0:
            if c[0] == 0:
                return False
        elif wall == 1:
            if c[1] == self.h - 1:
                return False
        elif wall == 2:
            if c[0] == self.w - 1:
                return False
        elif wall == 3:
            if c[1] == 0:
                return False
        return True

    def different_sets(self, cell, neighbor):
        """
        :param cell: cellule a tester
        :param neighbor: voisine
        :return: true si les deux cellules ne sont pas dans le meme ensemble
        """
        return self.grid[cell[0]][cell[1]].set != self.grid[neighbor[0]][neighbor[1]].set

    def remove_wall(self, c1, c2):
        """
        :return: supprime le mur entre c1 et c2
        """
        w = c1[2]
        self.grid[c1[0]][c1[1]].walls[w] = False
        self.grid[c2[0]][c2[1]].walls[(w + 2) % 4] = False


class Set:
    #ensemble d'ensembles de cellules
    def __init__(self, maze):  # {0: set([(f, o), (o, b), (a, r)...])}
        self.lst = {}
        rooms = maze.rooms
        for room in rooms:
            ind = maze.grid[room.top][room.left].set
            cellList = []
            for j in range(room.left, room.right + 1):
                for i in range(room.top, room.bottom + 1):
                    cellList.append((i, j))
            self.lst[ind] = set(cellList)

    def __str__(self):
        ch = ""
        for e in self.lst:
            for cell in self.lst[e]:
                ch += "(" + str(cell[0]) + ", " + str(cell[1]) + ")"
        return ch

    def already(self, ind, c):
        """teste si une cellule est deja dans l'ensemble de cellule"""
        if ind in self.lst:
            if c in self.lst[ind]:
                return True
        return False

    def join_sets(self, c1, c2, maze):
        #union de deux ensembles lorsque deux cellules sont dans des ensembles different
        set1 = maze.grid[c1[0]][c1[1]].set
        set2 = maze.grid[c2[0]][c2[1]].set
        if not self.already(set1, c1) and not self.already(set2, c2):
            #si aucune des cellule n'est dans un ensemble plus grand qu'elle meme
            self.lst[set1] = set([c1, c2])
            maze.grid[c2[0]][c2[1]].set = set1 #ensemble de la premiere cellule
        # si une des deux n'a pas d'ensemble
        elif not self.already(set1, c1):
            self.lst[set2].add(c1)
            maze.grid[c1[0]][c1[1]].set = set2 #deuxieme
        elif not self.already(set2, c2):
            self.lst[set1].add(c2)
            maze.grid[c2[0]][c2[1]].set = set1 #premiere
        else:
            #si le premier est plus grand que le deuxieme
            if len(self.lst[set1]) >= len(self.lst[set2]):
                #changement d'ensemble de chaque
                for e in self.lst[set2]:
                    maze.grid[e[0]][e[1]].set = set1
                setNb = set1
            else:
                for e in self.lst[set1]:
                    maze.grid[e[0]][e[1]].set = set2
                setNb = set2
            #union des deux ensembles
            setInt = set.union(self.lst[set1], self.lst[set2])
            del self.lst[set1]
            del self.lst[set2]
            self.lst[setNb] = setInt


def makeRandomWallList(maze):
    """Fais une liste de murs aleatoire (equivalent d'ajouter un poid aux murs)"""
    list = []
    for i in range(maze.w):
        for j in range(maze.h):
            for k in range(4):
                if maze.have_neighbor((i, j), k) and maze.grid[i][j].walls[k]:
                    list.append((i, j, k))
    #melange de la liste ordonnee
    shuffle(list)
    return list


def find_neighbor(cell):
    #trouve la case voisine d'une cellule par rapport a un mur
    x = cell[0]
    y = cell[1]
    wall = cell[2]
    if wall == 0:  # top
        xp = x - 1
        yp = y
    elif wall == 1:  # right
        xp = x
        yp = y + 1
    elif wall == 2:  # bottom
        xp = x + 1
        yp = y
    elif wall == 3:  # left
        xp = x
        yp = y - 1
    return (xp, yp)


def place_rooms(maze, roomRange):
    """
    :param maze: la grille de cellules
    :param roomRange: la taille d'une piece
    :return: des pieces dans le labyrinthe
    """
    r_min = roomRange[0]
    r_max = roomRange[1]

    x1 = randint(1, maze.w - 1 - r_max)
    y1 = randint(1, maze.h - 1 - r_max)
    width = randint(r_min, r_max)
    height = randint(r_min, r_max)
    x2 = x1 + width
    y2 = y1 + height
    #creation de la piece
    roomInt = Room(x1, y1, x2, y2)
    #si elle ne se superpose pas sur une autre
    if maze.non_overlap_room(roomInt):
        ind = maze.grid[x1][y1].set
        for i in range(x1, x2):
            for j in range(y1, y2):
                #ouverture de tous les murs
                maze.grid[i][j].walls = [False, False, False, False]
                #changement d'ensemble
                maze.grid[i][j].set = ind
                #si sur un bord
                if i == x1:
                    maze.grid[i][j].walls[0] = True
                if j == y2 - 1:
                    maze.grid[i][j].walls[1] = True
                if i == x2 - 1:
                    maze.grid[i][j].walls[2] = True
                if j == y1:
                    maze.grid[i][j].walls[3] = True
        maze.rooms.append(roomInt)


def kruskal(maze, roomsNb):
    """
    I - Create a list of all walls, and create a set for each cell, each containing just that one cell.
    II - For each wall, in some random order:
        1 - If the cells divided by this wall belong to distinct sets:
            a - Remove the current wall.
            b - Join the sets of the formerly divided cells.
    :param maze: le labyrinthe
    :param roomsNb: le nombre de piece a creer
    :return: un labyrinthe parfait avec en plus des salles
    """
    #algo de kruskal presente sur wikipedia
    roomRange = [5, 10]
    # STEP 0 place rooms
    for i in range(roomsNb):
        place_rooms(maze, roomRange)
    # STEP I
    # a-
    wallList = makeRandomWallList(maze)
    # b-
    cellSet = Set(maze)
    # STEP II
    for cell in wallList:  # cell with wall
        # step 1
        neighbor = find_neighbor(cell)
        if maze.different_sets(cell, neighbor):
            # step a
            maze.remove_wall(cell, neighbor)
            # step b
            cell = (cell[0], cell[1])
            cellSet.join_sets(cell, neighbor, maze)
    return maze

def create_maze(w, h, roomsNb, tresor):
    """
    :param w: largeur (hauteur pour l'affichage)
    :param h: hauteur (largeur)
    :param roomsNb: nombre de pieces
    :param tresor: si tresor ou non
    :return: un labyrinthe avec un tresor ou une sortie
    """
    maze = Grid(w, h, tresor)
    kruskal(maze, roomsNb)
    return maze