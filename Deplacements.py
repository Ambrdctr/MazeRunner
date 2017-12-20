import pygame
from pygame.locals import *

#Couleurs
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

color_mur = black
color_porte = green
color_cle = green
cases1 = blue
cases2 = white


#Dimensions
w = 7
h = 7
taille_perso = 100
taille_case = 100
deplacement = 100
largeur = taille_case * w
hauteur = taille_case * h
#dimensions fenetre
wbis = 5
hbis = 5
largeurBis = taille_case * wbis
hauteurBis = taille_case * hbis


"""pygame.init()

#Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((largeurBis, hauteurBis))

#Fond
gazon = pygame.image.load("gazon.jpg").convert()
#screen.blit(fond, (0,0))
#Placement personnage"""
x = 0
y = 0
perso = pygame.image.load("perso.png").convert_alpha()  #convert_alpha = zone transparente



#ex = [([True,False,False,False],'eau'),([True,True,False,False],'gazon')]


cles = [(1,1)]

carte = create_maze(w,h)
         


def draw_map(tab):
    
    pos2 = 0
    
    for i in range ((y//taille_case - 2), (y//taille_case + 3)):
        pos1 = 0
        for k in range ((x//taille_case - 2), (x//taille_case + 3)):
            if i in range(0,len(tab)) and k in range(0,len(tab[i])):
                if tab[i][k].state == 'v':
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    screen.blit(gazon, (posx,posy))
                    ##Si mur
                if tab[i][k].walls[0] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx, posy-5, taille_case, 10), 0)
                if tab[i][k].walls[1] == True:
                    posx = taille_case * pos1 + taille_case
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx-5, posy, 10, taille_case), 0)
                if tab[i][k].walls[2] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2 + taille_case
                    pygame.draw.rect(screen, color_mur, (posx, posy-5, taille_case, 10), 0)
                if tab[i][k].walls[3] == True:
                    posx = taille_case * pos1
                    posy = taille_case * pos2
                    pygame.draw.rect(screen, color_mur, (posx-5, posy, 10, taille_case), 0)
            if (k == x//taille_case) and (i == y/taille_case):
                posx = taille_case * pos1
                posy = taille_case * pos2
                screen.blit(perso, (posx,posy))
            pos1 += 1
        pos2 += 1
                        
                                    
                
                
            
draw_map(carte)



#Chargement et collage de la clée
have_key = False
key = pygame.image.load("cle.png").convert_alpha()
def draw_cle(tab):
    global key
    for elt in tab:
        posx = taille_case * elt[0]
        posy = taille_case * elt[1]
        screen.blit(key, (posx, posy))
        
        
draw_cle(cles)



def mur(x,y,direction):
    res = False
    yPrec = int(y / taille_case)
    xPrec = int(x / taille_case)
    if direction=='haut':
        ySuiv = int((y - taille_case) / taille_case)
        if yPrec != ySuiv and carte[yPrec][xPrec].walls[0]==True:
            res = True            
    if direction=='droite':
        xSuiv = int((x + taille_case) / taille_case) 
        if xPrec != xSuiv and carte[yPrec][xPrec].walls[1]==True:
            res = True
    if direction=='bas':
        ySuiv = int((y + taille_case) / taille_case)
        if yPrec != ySuiv and carte[yPrec][xPrec].walls[2]==True:
            res = True
    if direction=='gauche':
        xSuiv = int((x - taille_case) / taille_case)
        if xPrec != xSuiv and carte[yPrec][xPrec].walls[3]==True:
            res = True
    return res





def cle(x,y):
    global have_key
    ybis = int(y / taille_case)
    xbis = int(x / taille_case)
    for elt in cles:
        if elt == (xbis,ybis):
            have_key = True
            exit
    return


#Rafraîchissement de l'écran
pygame.display.flip()

#Touche reste enfoncée
pygame.key.set_repeat(400,50)

#Boucle infinie
running = True
while running:
    for event in pygame.event.get():
        #Lorsque l'on ferme la fenetre
        if event.type == QUIT:
            running = False
        #Deplacement
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if (y-deplacement)>=0 and not mur(x, y, 'haut'):
                    # if not have_key:
                    #    print("Il vous manque la cle !")
                    #else:
                        y-=deplacement
                
                    
            if event.key == K_DOWN:
                if (y+deplacement)<hauteur and not mur(x, y, 'bas'):
                   # if not have_key :
                   #     print("Il vous manque la cle !")
                   # else:
                        y+=deplacement
                
                    
            if event.key == K_RIGHT:
                if (x+deplacement)<largeur and not mur(x, y, 'droite'):
                   # if not have_key :
                   #     print("Il vous manque la cle !")
                   # else:
                        x+=deplacement
                
                    
            if event.key == K_LEFT:
                if (x-deplacement)>=0 and not mur(x, y, 'gauche'):
                   # if not have_key :
                   #     print("Il vous manque la cle !")
                   # else:
                        x-=deplacement



                
            #Re-collage
            pygame.draw.rect(screen, color_mur, (0, 0, w*taille_case, h*taille_case), 0)
            screen.blit(screen, (0,0))
            cle(x,y)
            draw_map(carte)
            if not have_key:
                draw_cle(cles)
            #screen.blit(perso, (x,y))
            #Rafraichissement
            pygame.display.flip()
pygame.display.quit()
