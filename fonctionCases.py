def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entreeDonjon'

def allerEtageSuivant(map, perso):

    if map.grid[perso.y][perso.x].state == 'sortie':
        tab = map.grid
        for i in range(0, len(tab)):
            for k in range(0, len(tab[i])):
                if tab[i][k].visitee != True and tab[i][k].visitee != False:
                    tab[i][k].visitee = True
        return True
    else:
        return False


def allerEtagePrecedent(map, perso):

    return map.grid[perso.y][perso.x].state == 'entree'

def victoire(map, perso):

    return map.grid[perso.y][perso.x].state == 'tresor'