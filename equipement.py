import pygame
from pygame.locals import *
from classObject import Epee, Couteau, PotionVie, PotionForce, PotionMemoire, PotionVitesse
from affichage import afficherStats
import random

def inventaire(screen, perso):
    # Opacité de l'arrière plan
    s = pygame.Surface((1600, 900))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    afficherStats(screen, perso)
    posObjEquipement = perso.afficherEquipement(screen)

    posObjInventaire = perso.inventaire.afficher_sac("Inventaire")

    run = True

    while run:

        for event in pygame.event.get():

            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_i:
                    run = False

            pos = pygame.mouse.get_pos()
            conteneur = 0
            if posObjInventaire[1].collidepoint(pos):
                conteneur = 1
            elif posObjEquipement[1].collidepoint(pos):
                conteneur = 2

            if event.type == MOUSEBUTTONUP and event.button == 1:

                if conteneur == 1:
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            index = posObjInventaire[0].index(rect)
                            obj = perso.inventaire.tabObj[index]
                            if obj != False:
                                if isinstance(obj, Epee) or isinstance(obj, Couteau):
                                    perso.inventaire.tabObj[index] = perso.equipement[2]
                                    if perso.equipement[2] != False:
                                        perso.inventaire.contenu.append(perso.equipement[2])
                                    perso.equipement[2] = obj
                                    perso.inventaire.contenu.remove(obj)
                            break
                    perso.inventaire.afficher_sac("Inventaire")
                    perso.afficherEquipement(screen)


                elif conteneur == 2:
                    for rect in posObjEquipement[0]:
                        if rect.collidepoint(pos):
                            index = posObjEquipement[0].index(rect)
                            obj = perso.equipement[index]
                            if len(perso.inventaire.contenu) < perso.inventaire.capacite:
                                if isinstance(obj, Epee) or isinstance(obj, Couteau):
                                    perso.equipement[2] = False
                                    perso.inventaire.contenu.append(obj)
                                    for i in range(len(perso.inventaire.tabObj)):
                                        if perso.inventaire.tabObj[i] == False:
                                            perso.inventaire.tabObj[i] = obj
                                            break
                                break
                    perso.afficherEquipement(screen)
                    perso.inventaire.afficher_sac("Inventaire")
                perso.force = random.randint(4, 8)
                if perso.equipement[2] != False:
                    perso.force += perso.equipement[2].force
                afficherStats(screen, perso)

            if event.type == MOUSEMOTION:

                if conteneur == 1:
                    dansCase = False
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            perso.inventaire.afficher_sac("Inventaire", posObjInventaire[0].index(rect) + 1)
                            dansCase = True
                            break
                    if not dansCase:
                        perso.inventaire.afficher_sac("Inventaire")

                elif conteneur == 2:
                    dansCase = False
                    for rect in posObjEquipement[0]:
                        if rect.collidepoint(pos):
                            perso.afficherEquipement(screen, posObjEquipement[0].index(rect) + 1)
                            dansCase = True
                            break
                    if not dansCase:
                        perso.afficherEquipement(screen)

                else:
                    perso.afficherEquipement(screen)
                    perso.inventaire.afficher_sac("Inventaire")