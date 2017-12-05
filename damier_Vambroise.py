import pygame
from pygame.locals import *
from Maze import create_maze

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
w = 10
h = 10
taille_perso = 100
taille_case = 100
deplacement = 100
largeur = taille_case * w
hauteur = taille_case * h


pygame.init()

#Ouverture de la fenêtre Pygame
screen = pygame.display.set_mode((largeur, hauteur))

#Fond
fond = pygame.image.load("background.jpg").convert()
screen.blit(fond, (0,0))


#ex = [([True,False,False,False],'eau'),([True,True,False,False],'gazon')]


cles = [(1,1)]


#carte = [[([False,False,False,False],'eau'),([False,True,False,False],'gazon'),([False,True,True,True],'gazon'),([False,False,False,True],'gazon')],
#         [([False,False,False,False],'eau'),([False,False,False,False],'gazon'),([True,False,False,False],'gazon'),([False,False,False,False],'gazon')],
#         [([False,False,False,False],'eau'),([False,False,False,False],'gazon'),([False,False,False,False],'gazon'),([False,False,False,False],'gazon')],
#         [([False,False,False,False],'eau'),([True,False,False,False],'gazon'),([False,False,False,False],'gazon'),([False,False,False,False],'gazon')]]
        


carte = create_maze(w,h)
         



def draw_map(tab):
    for i in range (0,len(tab)):
        for k in range (0,len(tab[i])):
                if tab[i][k].walls[0] == True:          ##Si mur
                    posx = taille_case * k 
                    posy = taille_case * i
                    pygame.draw.rect(screen, color_mur, (posx, posy-5, taille_case, 10), 0)
                if tab[i][k].walls[1] == True:
                    posx = taille_case * k + taille_case
                    posy = taille_case * i 
                    pygame.draw.rect(screen, color_mur, (posx-5, posy, 10, taille_case), 0)
                if tab[i][k].walls[2] == True:
                    posx = taille_case * k 
                    posy = taille_case * i + taille_case
                    pygame.draw.rect(screen, color_mur, (posx, posy-5, taille_case, 10), 0)
                if tab[i][k].walls[3] == True:
                    posx = taille_case * k
                    posy = taille_case * i 
                    pygame.draw.rect(screen, color_mur, (posx-5, posy, 10, taille_case), 0)

                        
                                    
                
                
            
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



##MODIFIER LA FONCTION PORTE CAR PAS BONNE
def porte(x,y):
    res = False
    ybis = int(y / taille_case)
    xbis = int(x / taille_case)
    if carte[ybis][xbis] != 0:
        if carte[ybis][xbis].state == 'porte':
            res = True
            exit
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

#Chargement et collage du pion
x = 0
y = 0
perso = pygame.image.load("perso.png").convert_alpha()  #convert_alpha = zone transparente
screen.blit(perso, (x,y))

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
                    if not have_key and porte(x, y-deplacement):
                        print("Il vous manque la cle !")
                    else:
                        y-=deplacement
                
                    
            if event.key == K_DOWN:
                if (y+2*deplacement)<hauteur and not mur(x, y, 'bas'):
                    if not have_key and porte(x, y+deplacement):
                        print("Il vous manque la cle !")
                    else:
                        y+=deplacement
                
                    
            if event.key == K_RIGHT:
                if (x+2*deplacement)<largeur and not mur(x, y, 'droite'):
                    if not have_key and porte(x+deplacement, y):
                        print("Il vous manque la cle !")
                    else:
                        x+=deplacement
                
                    
            if event.key == K_LEFT:
                if (x-deplacement)>=0 and not mur(x, y, 'gauche'):
                    if not have_key and porte(x-deplacement, y):
                        print("Il vous manque la cle !")
                    else:
                        x-=deplacement
                
            #Re-collage
            
            screen.blit(screen, (0,0))
            ##draw_damier()
            screen.blit(fond, (0,0))
            cle(x,y)
            draw_map(carte)
            if not have_key:
                draw_cle(cles)
            screen.blit(perso, (x,y))
            #Rafraichissement
            pygame.display.flip()
pygame.display.quit()
