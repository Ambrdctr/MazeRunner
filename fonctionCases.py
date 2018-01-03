def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entreeDonjon'

def allerEtageSuivant(map, perso):
    return map.grid[perso.y][perso.x].state == 'sortie'

def allerEtagePrecedent(map, perso):

    return map.grid[perso.y][perso.x].state == 'entree'

def victoire(map, perso):

    return map.grid[perso.y][perso.x].state == 'tresor'