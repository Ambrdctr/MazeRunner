import pygame
from pygame.locals import *
from classObject import Piece

def marchander(perso, marchand):

    screen = marchand.inventaire.ecran
    # Opacité de l'arrière plan
    s = pygame.Surface((1600, 900))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    posObjInventaire = perso.inventaire.afficher_sac(perso.nom)
    posObjMarchand = marchand.inventaire.afficher_stock(marchand.nom)

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
            if posObjMarchand[1].collidepoint(pos):
                conteneur = 2

            if event.type == MOUSEBUTTONUP and event.button == 1:

                if conteneur == 1 and marchand.nom == 'Acheteur':
                    for rect in posObjInventaire[0]:
                        print(rect)
                        if rect.collidepoint(pos):
                            index = posObjInventaire[0].index(rect)
                            obj = perso.inventaire.tabObj[index]
                            if obj != False:
                                if marchand.inventaire.pieces == 0:
                                    perso.inventaire.tabObj[index] = False
                                    perso.inventaire.contenu.remove(obj)
                                    listePiece = calculerValeurObj(obj, screen)
                                    for i in range(len(listePiece)):
                                        marchand.inventaire.tabObj[i] = listePiece[i]
                                        marchand.inventaire.contenu.append(listePiece[i])
                                        marchand.inventaire.pieces += listePiece[i].valeur
                            break
                    perso.inventaire.afficher_sac(perso.nom)
                    marchand.inventaire.afficher_stock(marchand.nom)


                elif conteneur == 2:
                    for rect in posObjMarchand[0]:
                        if rect.collidepoint(pos):
                            index = posObjMarchand[0].index(rect)
                            obj = marchand.inventaire.tabObj[index]
                            if obj != False:
                                if isinstance(obj, Piece):
                                    marchand.inventaire.tabObj[index] = False
                                    marchand.inventaire.contenu.remove(obj)
                                    marchand.inventaire.pieces -= obj.valeur
                                    perso.inventaire.pieces += obj.valeur
                                else:
                                    if (len(perso.inventaire.contenu) < perso.inventaire.capacite) and (perso.inventaire.pieces >= obj.valeur):
                                        perso.inventaire.contenu.append(obj)
                                        perso.inventaire.pieces -= obj.valeur
                                        for i in range(len(perso.inventaire.tabObj)):
                                            if perso.inventaire.tabObj[i] == False:
                                                perso.inventaire.tabObj[i] = obj
                                                break
                            break
                    marchand.inventaire.afficher_stock(marchand.nom)
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
                        marchand.inventaire.afficher_stock(marchand.nom)
                        perso.inventaire.afficher_sac(perso.nom)


                elif conteneur == 2:
                    dansCase = False
                    for rect in posObjMarchand[0]:
                        if rect.collidepoint(pos):
                            marchand.inventaire.afficher_stock(marchand.nom, posObjMarchand[0].index(rect)+1)
                            dansCase = True
                            break
                    if not dansCase:
                        marchand.inventaire.afficher_stock(marchand.nom)
                        perso.inventaire.afficher_sac(perso.nom)

                else:
                    marchand.inventaire.afficher_stock(marchand.nom)
                    perso.inventaire.afficher_sac(perso.nom)

            pygame.display.flip()

def calculerValeurObj(obj, screen):
    val = obj.valeur

    listePiece = []

    while val != 0:
        if val >= 50:
            listePiece.append(Piece(50, screen))
            val -= 50
        elif val >= 10:
            listePiece.append(Piece(10, screen))
            val -= 10
        elif val >= 5:
            listePiece.append(Piece(5, screen))
            val -= 5
        elif val >= 2:
            listePiece.append(Piece(2, screen))
            val -= 2
        elif val == 1:
            listePiece.append(Piece(1, screen))
            val -= 1

    return listePiece
