def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entreeDonjon'

def allerExterieur(map, perso):

    return map.grid[perso.y][perso.x].state == 'entree'

def allerEtageSuivant(map, perso):
    return map.grid[perso.y][perso.x].state == 'sortie'

def victoire(map, perso):

    return map.grid[perso.y][perso.x].state == 'tresor'