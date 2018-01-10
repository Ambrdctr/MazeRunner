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
from message import ecrire
from menu import victoire_screen
import random
import time

def play(screen, difficulty):
    screen.fill((50, 50, 50))

    time_start = time.time()
    exterieur = create_empty_map()
    etages = [exterieur]
    k = 0  # Permet de savoir jusqu'à quel étage est arrivé le joueur
    e = 0 # Permet de connaitre l'etage courant du joueur

    map = etages[e]

    perso = Joueur((3,1), 'Inventaire', screen)

    forgeron = Marchand('Forgeron', screen)
    sorciere = Marchand('Sorciere', screen)
    acheteur = Marchand('Acheteur', screen)

    aBouge = False

    # Touche reste enfoncée
    pygame.key.set_repeat(100, 50)

    arrive = True
    time_piece = time.time()
    run = True
    perso.derniereAtt = time.time()
    while run:

        size = screen.get_size()

        if size[0] <= size[1]:
            taille_case = size[0] // 12
        else:
            taille_case = size[1] // 12
        pygame.draw.rect(screen, (50, 50, 50), (0, taille_case*8, taille_case*13, size[1]-taille_case*8))

        if time.time() - time_piece >= 30:
            perso.inventaire.pieces += random.randint(3, 5)
            time_piece = time.time()

        pygame.time.Clock().tick(30)
        affichage(screen, perso, map.liste_monstres, map.liste_coffres, map)
        if arrive:
            ecrire("""Bonjour aventurier !\nTon but est de retrouver le trésor du donjon\nBonne chance...\n\nNote que ton travail te rapportera entre 3 et 5 pièces toutes les 30 secondes !""",
                   screen)
            arrive = False
        gererEquipement(screen, perso)
        # Rafraîchissement de l'écran
        pygame.display.flip()

        if aBouge and victoire(map, perso):
            aBouge = False
            if perso.aCle():
                perso.supprimerCle()
                time.sleep(1)
                victoire_screen(screen, time.time()-time_start)
                run = False
            else:
                ecrire(
                    """Il vous faut une clé pour ouvrir le trésor !\nVous n'en avez pas acheté chez le forgeron ou l'avez déjà utilisée.""",
                    screen)

        if not perso.vivant :
            time.sleep(1)
            size = screen.get_size()
            wasted = pygame.image.load("images/wasted.png").convert_alpha()
            wasted = pygame.transform.scale(wasted, (size[0], size[1]))
            screen.blit(wasted, (0,0))
            pygame.display.flip()
            while run:

                for event in pygame.event.get():

                    # Lorsque l'on ferme la fenetre
                    if event.type == QUIT:
                        run = False
                    if event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            run = False

                    if event.type == MOUSEBUTTONUP and event.button == 1:
                        run = False

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
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = not pause(screen)
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    aBouge = deplacerPerso(perso, map, map.liste_monstres, map.liste_coffres, event.key)
                if event.key == K_i:
                    inventaire(screen, perso)


        if perso.dansDonjon:
            if map.grid[perso.y][perso.x].visitee != True:
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


        etageSuivant = allerEtageSuivant(map, perso)
        if aBouge and (etageSuivant or sortieTrouve(map, perso) or allerDonjon(map, perso)):
            if etageSuivant and not perso.aCle():
                aBouge = False
                ecrire("Il vous faut une clé pour continuer! Vous n'en avez pas acheté chez le forgeron ou l'avez déjà utilisée.",
                           screen)
            elif etageSuivant and perso.aCle():
                perso.supprimerCle()
                map.grid[perso.y][perso.x].state = 'sortie'
            else:
                aBouge = False
                e += 1
                if e > k:
                    if k < difficulty:
                        etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, False)) #sans le tresor
                    else:
                        etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, True)) #avec le tresor
                    k += 1
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