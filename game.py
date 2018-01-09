import pygame
from pygame.locals import *
from map import create_empty_map
from affichage import affichage, pause
from equipement import inventaire, gererEquipement
from deplacements import deplacerPerso, deplacerMonstre
from classPerso import Perso, Joueur, Marchand, Monstre
from classChest import Chest
from fonctionCases import *
from labyrinthe import create_maze
from menu import sortir
from marchandage import marchander
<<<<<<< HEAD
from message import ecrire
from menu import victoire_screen
=======

>>>>>>> Ambroise
import random
import time

def play(screen, difficulty):

    victoire_screen(screen, 13407)

    time_start = time.time()
    out = True
    exterieur = create_empty_map()
    etages = [exterieur]
    k = 0  # Permet de savoir jusqu'à quel étage est arrivé le joueur
    e = 0 # Permet de connaitre l'etage courant du joueur

    map = etages[e]

    perso = Joueur((3,1), 'Joueur', screen)

    forgeron = Marchand('Forgeron', screen)
    sorciere = Marchand('Sorciere', screen)
    acheteur = Marchand('Acheteur', screen)

    forgeron = Marchand('Forgeron', screen)
    sorciere = Marchand('Sorciere', screen)
    acheteur = Marchand('Acheteur', screen)

    aBouge = False

    # Touche reste enfoncée
    pygame.key.set_repeat(100, 50)

    arrive = True
    while out:
        pygame.time.Clock().tick(30)
        screen.fill((0, 0, 0))
        affichage(screen, perso, map.liste_monstres, map.liste_coffres, map)
<<<<<<< HEAD
        if arrive:
            ecrire("""Bonjour aventurier !\nRetrouvera-tu le trésor ?\nBonne chance...""",
                   screen)
            arrive = False

=======
>>>>>>> Ambroise
        gererEquipement(screen, perso)
        # Rafraîchissement de l'écran
        pygame.display.flip()

        if victoire(map,perso):
            time.sleep(1)
            out = victoire_screen(screen, time.time()-time_start)
            time.sleep(3)
            perso.x = 0
            perso.y = 0
            map = exterieur
            perso.dansDonjon = False
            e = 0

        if not perso.vivant :
            time.sleep(1)
            wasted = pygame.image.load("images/wasted.png").convert_alpha()
            wasted = pygame.transform.scale(wasted, (1600,900))
            screen.blit(wasted, (0,0))
            pygame.display.flip()
            time.sleep(5)
            out = False

        if not perso.dansDonjon:
            if surForgeron(map, perso) and aBouge:
                marchander(perso, forgeron)
                aBouge = False
            elif surSorciere(map, perso) and aBouge:
                marchander(perso, sorciere)
                aBouge = False
            elif surAcheteur(map, perso) and aBouge:
                marchander(perso, acheteur)
                aBouge = False


        for event in pygame.event.get():
            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                out = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    out = not pause(screen)
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    aBouge = deplacerPerso(perso, map, map.liste_monstres, map.liste_coffres, event.key)
                if event.key == K_i:
                    inventaire(screen, perso)


        if perso.dansDonjon:
<<<<<<< HEAD
            if not map.grid[perso.y][perso.x].visitee:
=======
            if map.grid[perso.y][perso.x].visitee != True:
>>>>>>> Ambroise
                map.grid[perso.y][perso.x].visitee = time.time()
            piece = map.est_dans_piece((perso.x, perso.y))
            if piece != False:
                piece.visite_cellules_piece(map.grid)
                if not piece.visitee:
                    coords = piece.renvoi_diff_coords(difficulty)
                    for coord in coords:
                        map.liste_monstres.append(Monstre(coord, difficulty))
                    coffre_coord = piece.coord_border(map.grid)
                    map.liste_coffres.append(Chest(coffre_coord[0][1], coffre_coord[0][0], coffre_coord[1], screen))
                    piece.visitee = True
            for monstre in map.liste_monstres:
                if monstre.vivant:
                    if time.time() - monstre.dernierMvmt >= monstre.vitesse:
                        monstre.dernierMvmt = time.time()
                        deplacerMonstre(monstre, map.liste_monstres, map.liste_coffres, map, perso)

        if aBouge and (allerEtageSuivant(map, perso) or allerDonjon(map, perso)):
            e += 1
            if e > k:
                if k < difficulty:
                    etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, False)) #sans le tresor
                else:
                    etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, True)) #avec le tresor
                k += 1
            aBouge = False
            donjon = etages[e]
            map = donjon
            perso.x = map.start[1]
            perso.y = map.start[0]
            perso.dansDonjon = True

        if allerEtagePrecedent(map, perso):
            if aBouge:
                if e == 1:
                    if sortir(screen):
                        perso.x = 0
                        perso.y = 0
                        e -= 1
                        map = etages[e]
                        perso.dansDonjon = False
                    else:
                        aBouge = False
                else:
                    aBouge = False
                    e -= 1
                    donjon = etages[e]
                    map = donjon
                    perso.x = map.end[1]
                    perso.y = map.end[0]
    return out