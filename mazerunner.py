import pygame
from pygame.locals import *
import time
from menu import startMenu#, options, credit

def principal():
    run = True
    while run:
        startMenu()
        choice = startMenu()
        if choice == 1:
            play()
        elif choice == 2:
            options()
        elif choice == 3:
            run = False
    credit()
    time.sleep(5)
    pygame.display.quit()


