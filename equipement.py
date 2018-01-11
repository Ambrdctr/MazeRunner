import pygame
from pygame.locals import *
from classObject import Epee, Couteau,  PotionVie, PotionForce, PotionMemoire, PotionVitesse, Casque, Heaume
from affichage import afficherStats
import random
import time

def inventaire(screen, perso):
    # Opacité de l'arrière plan

    size = screen.get_size()
    s = pygame.Surface((size[0], size[1]))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (0, 0))


    #actualisation de l'affichage
    afficherStats(screen, perso)
    posObjEquipement = perso.afficherEquipement(screen)
    posObjInventaire = perso.inventaire.afficher_sac(perso.nom)

    run = True

    while run:

        #actualisation par rapport a l'equipement du joueur
        gererEquipement(screen, perso)

        for event in pygame.event.get():

            # Lorsque l'on ferme la fenetre
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE or event.key == K_i:
                    run = False

            #position de la souris
            pos = pygame.mouse.get_pos()
            conteneur = 0
            # inventaire
            if posObjInventaire[1].collidepoint(pos):
                conteneur = 1
            #equipement
            elif posObjEquipement[1].collidepoint(pos):
                conteneur = 2

            if event.type == MOUSEBUTTONUP and event.button == 1:

                #sepuis l'inventaire
                if conteneur == 1:
                    for rect in posObjInventaire[0]:
                        if rect.collidepoint(pos):
                            index = posObjInventaire[0].index(rect)
                            obj = perso.inventaire.tabObj[index]
                            #si objet
                            if obj != False:
                                #si arme
                                if isinstance(obj, Epee) or isinstance(obj, Couteau):
                                    # peut etre False si rien d'equipe
                                    perso.inventaire.tabObj[index] = perso.equipement[2]
                                    # si il y a un objet sur la case des armes
                                    if perso.equipement[2] != False:
                                        perso.inventaire.contenu.append(perso.equipement[2])
                                    #ajout de l'equipement
                                    perso.equipement[2] = obj
                                    #suppression de l'objet dans le contenu
                                    perso.inventaire.contenu.remove(obj)
                                #si protection
                                elif isinstance(obj, Casque) or isinstance(obj, Heaume):
                                    perso.inventaire.tabObj[index] = perso.equipement[0]
                                    if perso.equipement[0] != False:
                                        perso.inventaire.contenu.append(perso.equipement[0])
                                    perso.equipement[0] = obj
                                    perso.inventaire.contenu.remove(obj)
                                #si potion (sauf sante)
                                elif (isinstance(obj, PotionVitesse) or isinstance(obj, PotionForce) or isinstance(obj, PotionMemoire)) and perso.equipement[1] == False:
                                    perso.inventaire.tabObj[index] = False
                                    perso.equipement[1] = obj
                                    perso.inventaire.contenu.remove(obj)
                                    obj.temps = time.time()
                                #si potion de sante
                                elif isinstance(obj, PotionVie):
                                    #mise a jour des points de vie
                                    if perso.vie < 100-obj.vie:
                                        perso.vie += obj.vie
                                    else:
                                        #ne peut pas depasser 100
                                        perso.vie = 100
                                    #suppression dans l'inventaire
                                    perso.inventaire.tabObj[index] = False
                                    perso.inventaire.contenu.remove(obj)
                            break

                elif conteneur == 2:
                    for rect in posObjEquipement[0]:
                        if rect.collidepoint(pos):
                            index = posObjEquipement[0].index(rect)
                            obj = perso.equipement[index]
                            if len(perso.inventaire.contenu) < perso.inventaire.capacite:
                                #on ne peut pas enlever une potion, elle s'enlevera toute seule une fois l'effet dissipe
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
                perso.inventaire.afficher_sac(perso.nom)
                perso.afficherEquipement(screen)

            if event.type == MOUSEMOTION:

                #meme principe de surbrillance que pour les echanges
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
        pygame.display.flip()

def gererEquipement(screen, perso):
    #stats initiles
    perso.resetStats()
    #actualisation
    #protection
    if perso.equipement[0] != False:
        if perso.equipement[0].protection > 0:
            perso.protection += perso.equipement[0].protection
        else:
            perso.equipement[0] = False
    #potions
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
    #armes
    if perso.equipement[2] != False:
        perso.force += perso.equipement[2].force
    #affichage
    afficherStats(screen, perso)