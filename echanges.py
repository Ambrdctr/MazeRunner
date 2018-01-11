import pygame
from pygame.locals import *
from classObject import Piece
from message import ecrire

def echange(perso, coffre):

    screen = coffre.ecran
    # Opacité de l'arrière plan

    size = screen.get_size()
    s = pygame.Surface((size[0], size[1]))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    #recuperation des positions des objets pour les clics et affichage des inventaires
    posObjInventaire = perso.inventaire.afficher_sac(perso.nom)
    #affichage du contenu du coffre
    posObjCoffre = coffre.afficher_contenu("Coffre")

    run = True
    while run:

        for event in pygame.event.get():

            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

            #recuperation de la position de la souris
            pos = pygame.mouse.get_pos()
            #recuperatino du conteneur (1 = inventaire, 2 = coffre
            conteneur = 0
            if posObjInventaire[1].collidepoint(pos):
                conteneur = 1
            elif posObjCoffre[1].collidepoint(pos):
                conteneur = 2

            #lorsque l'on clique et que l'on relache avec le boutton gauche
            if event.type == MOUSEBUTTONUP and event.button == 1:

                #inventaire
                if conteneur == 1:
                    for rect in posObjInventaire[0]:
                        #si clic sur une case
                        if rect.collidepoint(pos):
                            #recuperation de la position cliquee dans le sac
                            index = posObjInventaire[0].index(rect)
                            #recuperation de l'objet sur cette position
                            obj = perso.inventaire.tabObj[index]
                            #si il y a un objet
                            if obj != False:
                                #si le coffre peut contenir un nouvel objet
                                if len(coffre.contenu) < coffre.capacite:
                                    #on enleve l'objet du sac
                                    perso.inventaire.tabObj[index] = False
                                    perso.inventaire.contenu.remove(obj)
                                    #on l'ajoute au coffre
                                    coffre.contenu.append(obj)
                                    for i in range(len(coffre.tabObj)):
                                        #sur la premiere case libre
                                        if coffre.tabObj[i] == False:
                                            coffre.tabObj[i] = obj
                                            break
                                #si le coffre est plein
                                else:
                                    ecrire("Le coffre est plein !", screen)
                                    run = False
                            break
                    #actualisation de l'affichage
                    perso.inventaire.afficher_sac(perso.nom)
                    coffre.afficher_contenu("Coffre")

                #coffre
                elif conteneur == 2:
                    #meme principe que pour l'inventaire
                    for rect in posObjCoffre[0]:
                        if rect.collidepoint(pos):
                            index = posObjCoffre[0].index(rect)
                            obj = coffre.tabObj[index]
                            if obj != False:
                                #si c'est une piece alors ajouter a la bourse du joueur plutot que mettre dans l'inventaire
                                if isinstance(obj, Piece):
                                    #retire du coffre
                                    coffre.tabObj[index] = False
                                    coffre.contenu.remove(obj)
                                    perso.inventaire.pieces += obj.valeur
                                else:
                                    #si il y a au moins une place dans l'inventaire
                                    if len(perso.inventaire.contenu) < perso.inventaire.capacite:
                                        coffre.tabObj[index] = False
                                        coffre.contenu.remove(obj)
                                        perso.inventaire.contenu.append(obj)
                                        for i in range(len(perso.inventaire.tabObj)):
                                            if perso.inventaire.tabObj[i] == False:
                                                perso.inventaire.tabObj[i] = obj
                                                break
                                    else:
                                        ecrire("Votre inventaire est plein !", screen)
                                        run = False
                            break
                    coffre.afficher_contenu("Coffre")
                    perso.inventaire.afficher_sac(perso.nom)

            if event.type == MOUSEMOTION:

                #gestion affichage en surbrillance
                if conteneur == 1:
                    dansCase = False
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            #nouvel affichage
                            perso.inventaire.afficher_sac(perso.nom, posObjInventaire[0].index(rect)+1)
                            dansCase = True
                            break
                    if not dansCase:
                        #sors de la case, reaffichage
                        coffre.afficher_contenu("Coffre")
                        perso.inventaire.afficher_sac(perso.nom)

                #idem
                elif conteneur == 2:
                    dansCase = False
                    for rect in posObjCoffre[0]:
                        if rect.collidepoint(pos):
                            coffre.afficher_contenu("Coffre", posObjCoffre[0].index(rect)+1)
                            dansCase = True
                            break
                    if not dansCase:
                        coffre.afficher_contenu("Coffre")
                        perso.inventaire.afficher_sac(perso.nom)

                else:
                    coffre.afficher_contenu("Coffre")
                    perso.inventaire.afficher_sac(perso.nom)

            #actualisation de l'affichage
            pygame.display.flip()