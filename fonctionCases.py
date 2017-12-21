def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'escaliersbas'

def allerExterieur(map, perso):

    return map.grid[perso.y][perso.x].state == 'escaliershaut'

def victoire(map, perso):

    return map.grid[perso.y][perso.x].state == 'gagner'