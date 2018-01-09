import pygame
from pygame.locals import *
from classObject import Epee, Couteau,  PotionVie, PotionForce, PotionMemoire, PotionVitesse, Casque, Heaume
from affichage import afficherStats
import random
import time

def inventaire(screen, perso):
    # Opacité de l'arrière plan
    s = pygame.Surface((1600, 900))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))

    afficherStats(screen, perso)
    posObjEquipement = perso.afficherEquipement(screen)

    posObjInventaire = perso.inventaire.afficher_sac(perso.nom)

    run = True

    while run:

        gererEquipement(screen, perso)
        perso.inventaire.afficher_sac(perso.nom)
        perso.afficherEquipement(screen)

        pygame.display.flip()

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
                                elif isinstance(obj, Casque) or isinstance(obj, Heaume):
                                    perso.inventaire.tabObj[index] = perso.equipement[0]
                                    if perso.equipement[0] != False:
                                        perso.inventaire.contenu.append(perso.equipement[0])
                                    perso.equipement[0] = obj
                                    perso.inventaire.contenu.remove(obj)
                                elif (isinstance(obj, PotionVitesse) or isinstance(obj, PotionForce) or isinstance(obj, PotionMemoire)) and perso.equipement[1] == False:
                                    perso.inventaire.tabObj[index] = False
                                    perso.equipement[1] = obj
                                    perso.inventaire.contenu.remove(obj)
                                    obj.temps = time.time()
                                elif isinstance(obj, PotionVie):
                                    if perso.vie < 80:
                                        perso.vie += obj.vie
                                    else:
                                        perso.vie = 100
                                    perso.inventaire.tabObj[index] = False
                                    perso.inventaire.contenu.remove(obj)
                            break

                elif conteneur == 2:
                    for rect in posObjEquipement[0]:
                        if rect.collidepoint(pos):
                            index = posObjEquipement[0].index(rect)
                            obj = perso.equipement[index]
                            if len(perso.inventaire.contenu) < perso.inventaire.capacite:
                                if isinstance(obj, Epee) or isinstance(obj, Couteau):
                                    perso.equipement[2] = False
                                    for i in range(len(perso.inventaire.tabObj)):
                                        if perso.inventaire.tabObj[i] == False:
                                            perso.inventaire.tabObj[i] = obj
                                            break
                                    perso.inventaire.contenu.append(obj)
                                elif isinstance(obj, Casque) or isinstance(obj, Heaume):
                                    perso.equipement[0] = False
                                    for i in range(len(perso.inventaire.tabObj)):
                                        if perso.inventaire.tabObj[i] == False:
                                            perso.inventaire.tabObj[i] = obj
                                            break
                                    perso.inventaire.contenu.append(obj)
                                gererEquipement(screen, perso)
                                break

            if event.type == MOUSEMOTION:

                if conteneur == 1:
                    dansCase = False
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            perso.inventaire.afficher_sac(perso.nom, posObjInventaire[0].index(rect) + 1)
                            dansCase = True
                            break
                    if not dansCase:
                        perso.inventaire.afficher_sac(perso.nom)

                elif conteneur == 2:
                    dansCase = False
                    for rect in posObjEquipement[0]:
                        if rect.collidepoint(pos):
                            perso.afficherEquipement(screen, posObjEquipement[0].index(rect) + 1)
                            dansCase = True
                            break
                    if not dansCase:
                        perso.afficherEquipement(screen)

def gererEquipement(screen, perso):
    perso.resetStats()
    if perso.equipement[0] != False:
        if perso.equipement[0].protection > 0:
            perso.protection += perso.equipement[0].protection
        else:
            perso.equipement[0] = False
    if perso.equipement[1] != False:
        obj = perso.equipement[1]
        if isinstance(obj, PotionVitesse):
            perso.vitesse += obj.vitesse
            if not (obj.duree > time.time() - obj.temps):
                perso.equipement[1] = False
                perso.vitesse -= obj.vitesse
        if isinstance(obj, PotionForce):
            perso.force += obj.force
            if not (obj.duree > time.time() - obj.temps):
                perso.equipement[1] = False
                perso.force -= obj.force
        if isinstance(obj, PotionMemoire):
            perso.memoire += obj.memoire
            if not (obj.duree > time.time() - obj.temps):
                perso.equipement[1] = False
                perso.memoire -= obj.memoire
    if perso.equipement[2] != False:
        perso.force += perso.equipement[2].force
    afficherStats(screen, perso)