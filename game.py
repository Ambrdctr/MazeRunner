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

    #carte du monde exterieur
    exterieur = create_empty_map()
    #ajout comme etage 0
    etages = [exterieur]
    k = 0  # Permet de savoir jusqu'à quel étage est arrivé le joueur
    e = 0 # Permet de connaitre l'etage courant du joueur

    #carte affiche = exterieur
    map = etages[e]

    perso = Joueur((0,0), 'Inventaire', screen)
    #CHEATCODE************************************************************************************
    #perso.inventaire.pieces = 5000

    #creation des marchands
    forgeron = Marchand('Forgeron', screen)
    sorciere = Marchand('Sorciere', screen)
    acheteur = Marchand('Acheteur', screen)

    #permet de savoir si le joueur a bouge
    aBouge = False

    # Touche reste enfoncee
    pygame.key.set_repeat(100, 50)

    arrive = True
    time_start = time.time()
    time_piece = time.time()
    run = True
    perso.derniereAtt = time.time()
    while run:
        #affichage par rapport a la taille de la fenetre
        size = screen.get_size()

        if size[0] <= size[1]:
            taille_case = size[0] // 12
        else:
            taille_case = size[1] // 12
        pygame.draw.rect(screen, (50, 50, 50), (0, taille_case*8, taille_case*13, size[1]-taille_case*8))

        #ajout de piece toutes les 30 secondes
        if time.time() - time_piece >= 30:
            perso.inventaire.pieces += random.randint(3, 5)
            time_piece = time.time()

        #30 fps
        pygame.time.Clock().tick(30)
        #affichage du jeu
        affichage(screen, perso, map.liste_monstres, map.liste_coffres, map)

        #message d'arrivee
        if arrive:
            ecrire("""Bonjour aventurier !\nTon but est de retrouver le trésor du donjon\nBonne chance...\n\nNote que ta quete te rapportera entre 3 et 5 pièces toutes les 30 secondes !""",
                   screen)
            arrive = False
        gererEquipement(screen, perso)
        # Rafraîchissement de l'écran
        pygame.display.flip()

        #si le joueur trouve le tresor
        if aBouge and victoire(map, perso):
            aBouge = False
            #si il a la cle
            if perso.aCle():
                #utilisation pour ouvrir
                perso.supprimerCle()
                #affichage de l'ecran de victoire
                time.sleep(1)
                victoire_screen(screen, time.time()-time_start)
                #arret de la partie
                run = False
            else:
                #si pas de cle
                ecrire(
                    """Il vous faut une clé pour ouvrir le tresor !\nVous n'en avez pas acheté chez le forgeron ou l'avez déjà utilisée.""",
                    screen)

        #si le joueur est mort
        if not perso.vivant :
            time.sleep(1)
            size = screen.get_size()
            #affichage de l'ecran de mort
            wasted = pygame.image.load("images/wasted.png").convert_alpha()
            wasted = pygame.transform.scale(wasted, (size[0], size[1]))
            screen.blit(wasted, (0,0))
            pygame.display.flip()

            #boucle pour laisser quitter le joueur
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

        #si le perso n'est pas dans le donjon
        if not perso.dansDonjon:
            #si il est sur le forgeron
            if surForgeron(map, perso) and aBouge:
                #marchander avec le forgeron
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
                #pause
                if event.key == K_ESCAPE:
                    run = not pause(screen)
                #demande de mouvement
                if event.key == K_UP or event.key == K_DOWN or event.key == K_RIGHT or event.key == K_LEFT:
                    #deplacerPerso retourne vrai ou faux en fonction du deplacmeent (si possible ou non)
                    aBouge = deplacerPerso(perso, map, map.liste_monstres, map.liste_coffres, event.key)
                if event.key == K_i:
                    #affichage de l'inventaire
                    inventaire(screen, perso)

        #si le joueur est dans le donjon
        if perso.dansDonjon:
            #actualisation de la case courante avec le temps courant
            if map.grid[perso.y][perso.x].visitee != True:
                map.grid[perso.y][perso.x].visitee = time.time()
            #booleen permettant de savoir si le joueur est dans une piece
            piece = map.est_dans_piece((perso.x, perso.y))
            #si oui
            if piece != False:
                #affichage de la salle
                piece.visite_cellules_piece(map.grid)
                #si la piece n'a jamais ete visitee
                if not piece.visitee:
                    #renvoi des coordonnees aleatoire de la piece
                    coords = piece.renvoi_diff_coords(difficulty)
                    #positionnement aleatoire des monstre (peuvent tomber sur un coffre)
                    for coord in coords:
                        map.liste_monstres.append(Monstre(coord, difficulty))
                    #recuperation d'une case contre un mur aleatoire
                    coffre_coord = piece.coord_border(map.grid)
                    #positionnement du coffre sur cette case
                    map.liste_coffres.append(Chest(coffre_coord[0][1], coffre_coord[0][0], coffre_coord[1], screen))
                    #la piece est desormais visitee
                    piece.visitee = True
            #gestion du deplacement des monstre lorsqu'ils sont vivants
            for monstre in map.liste_monstres:
                if monstre.vivant:
                    if time.time() - monstre.dernierMvmt >= monstre.vitesse:
                        monstre.dernierMvmt = time.time()
                        deplacerMonstre(monstre, map.liste_monstres, map.liste_coffres, map, perso)

        #booleen permettant de savoir si le joueur veut aller un etage plus haut
        etageSuivant = allerEtageSuivant(map, perso)
        #si il a bouge et qu'il veut aller un etage plus haut
        if aBouge and (etageSuivant or sortieTrouve(map, perso) or allerDonjon(map, perso)):
            #si il y a une trappe et qu'il n'a pas la cle
            if etageSuivant and not perso.aCle():
                aBouge = False
                #affichage d'un message
                ecrire("Il vous faut une clé pour continuer! Vous n'en avez pas acheté chez le forgeron ou l'avez déjà utilisée.",
                           screen)
            #si trappe et cle
            elif etageSuivant and perso.aCle():
                #suppression de la cle
                perso.supprimerCle()
                #ouverture de l'etage
                map.grid[perso.y][perso.x].state = 'sortie'
            else:
                aBouge = False
                #actualisation de l'etage
                e += 1
                #si etage pas encore decouvert
                if e > k:
                    #creation d'un nouvel etage (tresor en fonction de la difficulte)
                    #difficile : etage 4
                    #moyen : etage 3
                    #facile : etage 2
                    if k < difficulty:
                        etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, False)) #sans le tresor
                    else:
                        etages.append(create_maze(difficulty*15, difficulty*20, difficulty*15, True)) #avec le tresor
                    k += 1
                #changement d'etage
                donjon = etages[e]
                map = donjon
                #positionnement sur l'entree
                perso.x = map.start[1]
                perso.y = map.start[0]
                perso.dansDonjon = True

        #quand le joueur veut changer d'etage
        if allerEtagePrecedent(map, perso):
            if aBouge:
                #si il est au premier etage
                if e == 1:
                    #demander si il veut sortir
                    if sortir(screen):
                        #postionnement a l'exterieur
                        perso.x = 4
                        perso.y = 2
                        perso.dir = 1
                        e -= 1
                        map = etages[e]
                        perso.dansDonjon = False
                    else:
                        aBouge = False
                else:
                    #positionnement a la sortie de l'etage precedent
                    aBouge = False
                    e -= 1
                    donjon = etages[e]
                    map = donjon
                    perso.x = map.end[1]
                    perso.y = map.end[0]