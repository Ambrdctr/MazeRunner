def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entree'

def allerExterieur(map, perso):

    return map.grid[perso.y][perso.x].state == 'sortie'