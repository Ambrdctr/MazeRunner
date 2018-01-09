from classObject import Cle
def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entreeDonjon'

def allerEtageSuivant(map, perso):

<<<<<<< HEAD
    if map.grid[perso.y][perso.x].state == 'trappe':
        aCle = False
        for obj in perso.inventaire.contenu:
            if isinstance(obj, Cle):
                perso.inventaire.contenu.remove(obj)
                index = perso.inventaire.tabObj.index(obj)
                perso.inventaire.tabObj[index] = False
                aCle = True
                break
        if aCle:
            map.grid[perso.y][perso.x].state = 'sortie'
            return True


    elif map.grid[perso.y][perso.x].state == 'sortie':
=======
    if map.grid[perso.y][perso.x].state == 'sortie':
>>>>>>> Ambroise
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
    aCle = False
    for obj in perso.inventaire.contenu:
        if isinstance(obj, Cle):
            perso.inventaire.contenu.remove(obj)
            index = perso.inventaire.tabObj.index(obj)
            perso.inventaire.tabObj[index] = False
            aCle = True
            break
    if aCle:
        return map.grid[perso.y][perso.x].state == 'tresor'
    else:
        return False

def surForgeron(map, perso):

    return map.grid[perso.y][perso.x].state == 'forgeron'

def surSorciere(map, perso):

    return map.grid[perso.y][perso.x].state == 'sorciere'

def surAcheteur(map, perso):

<<<<<<< HEAD
=======
    return map.grid[perso.y][perso.x].state == 'tresor'

def surForgeron(map, perso):

    return map.grid[perso.y][perso.x].state == 'forgeron'

def surSorciere(map, perso):

    return map.grid[perso.y][perso.x].state == 'sorciere'

def surAcheteur(map, perso):

>>>>>>> Ambroise
    return map.grid[perso.y][perso.x].state == 'acheteur'