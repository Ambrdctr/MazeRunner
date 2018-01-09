import pygame
from pygame.locals import *
import time

def ecrire(phrase, screen):
    size = screen.get_size()
    if size[0] <= size[1]:
        min = size[0]
        taille_case = size[0] // 12
    else:
        min = size[1]
        taille_case = size[1] // 12
    taille_police = min * 15 // 500

    x=0
    y=taille_case*6
    xp=taille_case*13
    yp=taille_case*8

    s = pygame.Surface((xp, yp))
    s.set_alpha(200)
    s.fill((0, 0, 0))
    screen.blit(s, (x, y))

    myfont = pygame.font.SysFont('Comic Sans MS', taille_police)
    for ligne in phrase.splitlines():
        textsurface = myfont.render(ligne, False, (200, 200, 200))
        screen.blit(textsurface, (x+5, y+5))
        y += taille_police + 3

    curseur = pygame.image.load("images/curseur.png").convert_alpha()
    curseur = pygame.transform.scale(curseur, (taille_case, taille_case))
    screen.blit(curseur, (taille_case*12, taille_case*6))

    pygame.display.flip()

    run = True
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