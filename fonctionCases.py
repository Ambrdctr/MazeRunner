from classObject import Cle

# fonctions permettant de faire certianes actions en fonction de la case ou se trouve le joueur
def allerDonjon(map, perso):

    return map.grid[perso.y][perso.x].state == 'entreeDonjon'

def allerEtageSuivant(map, perso):

    return map.grid[perso.y][perso.x].state == 'trappe'

def sortieTrouve(map, perso):

    #pour affichage du chemin vers la sortie de la minimap
    if map.grid[perso.y][perso.x].state == 'sortie':
        tab = map.grid
        for i in range(0, len(tab)):
            for k in range(0, len(tab[i])):
                if tab[i][k].visitee != True and tab[i][k].visitee != False:
                    tab[i][k].visitee = True
        return True
    return False


def allerEtagePrecedent(map, perso):

    return map.grid[perso.y][perso.x].state == 'entree'

def victoire(map, perso):

    return map.grid[perso.y][perso.x].state == 'tresor'

def surForgeron(map, perso):

    return map.grid[perso.y][perso.x].state == 'forgeron'

def surSorciere(map, perso):

    return map.grid[perso.y][perso.x].state == 'sorciere'

def surAcheteur(map, perso):

    return map.grid[perso.y][perso.x].state == 'acheteur'