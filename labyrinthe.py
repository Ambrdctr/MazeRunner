from random import *

class Cell:
    # Constructor
    def __init__(self, i):
        self.walls = [True, True, True, True]
        self.state = 'pierre'
        self.set = i


class Room:
    # Constructor
    def __init__(self, x1, y1, x2, y2):
        self.left = y1
        self.right = y2 - 1
        self.top = x1
        self.bottom = x2 - 1

    def __str__(self):
        return "(" + str(self.left) + "," + str(self.top) + "), (" + str(self.right) + "," + str(self.bottom) + ")"


class Grid:
    def __init__(self, w, h):
        self.w = w
        self.h = h
        randList = [(0, 0), (0, self.h - 1), (self.w - 1, self.h - 1), (self.w - 1, 0)]
        self.start = choice(randList)
        randList.remove(self.start)
        self.end = choice(randList)
        self.rooms = []
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
        grid[self.end[0]][self.end[1]].state = 'sortie'
        self.grid = grid

    def non_overlap_room(self, roomB):
        for roomA in self.rooms:
            if not (roomB.left > roomA.right or
                            roomB.right < roomA.left or
                            roomB.top > roomA.bottom or
                            roomB.bottom < roomA.top):
                return False
        return True

    def is_in_room(self, cell):
        for roomA in self.rooms:
            if (roomA.left < cell[0] and
                        roomA.right > cell[0] and
                        roomA.top > cell[1] and
                        roomA.bottom < cell[1]):
                return True
        return False

    def have_neighbor(self, c, wall):
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
        return self.grid[cell[0]][cell[1]].set != self.grid[neighbor[0]][neighbor[1]].set

    def remove_wall(self, c1, c2):
        w = c1[2]
        self.grid[c1[0]][c1[1]].walls[w] = False
        self.grid[c2[0]][c2[1]].walls[(w + 2) % 4] = False


class Set:
    def __init__(self, maze):  # {0: set([(f, o), (o, b), (a, r)...])}
        self.lst = {}
        rooms = maze.rooms
        for room in rooms:
            ind = maze.grid[room.left][room.top].set
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
        if ind in self.lst:
            if c in self.lst[ind]:
                return True
        return False

    def join_sets(self, c1, c2, maze):
        set1 = maze.grid[c1[0]][c1[1]].set
        set2 = maze.grid[c2[0]][c2[1]].set
        if not self.already(set1, c1) and not self.already(set2, c2):
            self.lst[set1] = set([c1, c2])
            maze.grid[c2[0]][c2[1]].set = set1
        elif not self.already(set1, c1):
            self.lst[set2].add(c1)
            maze.grid[c1[0]][c1[1]].set = set2
        elif not self.already(set2, c2):
            self.lst[set1].add(c2)
            maze.grid[c2[0]][c2[1]].set = set1
        else:
            if len(self.lst[set1]) >= len(self.lst[set2]):
                for e in self.lst[set2]:
                    maze.grid[e[0]][e[1]].set = set1
                setNb = set1
            else:
                for e in self.lst[set1]:
                    maze.grid[e[0]][e[1]].set = set2
                setNb = set2
            setInt = set.union(self.lst[set1], self.lst[set2])
            del self.lst[set1]
            del self.lst[set2]
            self.lst[setNb] = setInt


def makeRandomWallList(maze):
    list = []
    for i in range(maze.w):
        for j in range(maze.h):
            for k in range(4):
                if maze.have_neighbor((i, j), k) and maze.grid[i][j].walls[k]:
                    list.append((i, j, k))
    shuffle(list)
    return list


def find_neighbor(cell):
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
    r_min = roomRange[0]
    r_max = roomRange[1]
    maxind = maze.w * maze.h

    x1 = randint(1, maze.w - 1 - r_max)
    y1 = randint(1, maze.h - 1 - r_max)
    width = randint(r_min, r_max)
    height = randint(r_min, r_max)
    x2 = x1 + width
    y2 = y1 + height
    roomInt = Room(x1, y1, x2, y2)
    if maze.non_overlap_room(roomInt):
        ind = maze.grid[x1][y1].set
        for i in range(x1, x2):
            for j in range(y1, y2):
                maze.grid[i][j].walls = [False, False, False, False]
                maze.grid[i][j].set = ind
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

def create_maze(w, h, roomsNb):
    maze = Grid(w, h)
    kruskal(maze, roomsNb)
    return maze