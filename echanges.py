import pygame
from pygame.locals import *
from classObject import Piece

def echange(perso, coffre):

    screen = coffre.ecran
    # Opacité de l'arrière plan

    size = screen.get_size()
    s = pygame.Surface((size[0], size[1]))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    posObjInventaire = perso.inventaire.afficher_sac(perso.nom)
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

            pos = pygame.mouse.get_pos()
            conteneur = 0
            if posObjInventaire[1].collidepoint(pos):
                conteneur = 1
            elif posObjCoffre[1].collidepoint(pos):
                conteneur = 2

            if event.type == MOUSEBUTTONUP and event.button == 1:

                if conteneur == 1:
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            index = posObjInventaire[0].index(rect)
                            obj = perso.inventaire.tabObj[index]
                            if obj != False:
                                if len(coffre.contenu) < coffre.capacite:
                                    perso.inventaire.tabObj[index] = False
                                    perso.inventaire.contenu.remove(obj)
                                    coffre.contenu.append(obj)
                                    for i in range(len(coffre.tabObj)):
                                        if coffre.tabObj[i] == False:
                                            coffre.tabObj[i] = obj
                                            break
                            break
                    perso.inventaire.afficher_sac(perso.nom)
                    coffre.afficher_contenu("Coffre")


                elif conteneur == 2:
                    for rect in posObjCoffre[0]:
                        if rect.collidepoint(pos):
                            index = posObjCoffre[0].index(rect)
                            obj = coffre.tabObj[index]
                            if obj != False:
                                if isinstance(obj, Piece):
                                    coffre.tabObj[index] = False
                                    coffre.contenu.remove(obj)
                                    perso.inventaire.pieces += obj.valeur
                                else:
                                    if len(perso.inventaire.contenu) < perso.inventaire.capacite:
                                        coffre.tabObj[index] = False
                                        coffre.contenu.remove(obj)
                                        perso.inventaire.contenu.append(obj)
                                        for i in range(len(perso.inventaire.tabObj)):
                                            if perso.inventaire.tabObj[i] == False:
                                                perso.inventaire.tabObj[i] = obj
                                                break
                            break
                    coffre.afficher_contenu("Coffre")
                    perso.inventaire.afficher_sac(perso.nom)

            if event.type == MOUSEMOTION:

                if conteneur == 1:
                    dansCase = False
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            perso.inventaire.afficher_sac(perso.nom, posObjInventaire[0].index(rect)+1)
                            dansCase = True
                            break
                    if not dansCase:
                        coffre.afficher_contenu("Coffre")
                        perso.inventaire.afficher_sac(perso.nom)


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

            pygame.display.flip()


