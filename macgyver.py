"""Main module for macgyver game"""

import pygame
from classes import *
from pygame.locals import *


def run_game():
    """Main function for running the game"""

    #~ Get level structure in list
    current_level = Level('level')

    #Initialisation de la bibliothèque Pygame
    pygame.init()

    #~ Window creation
    screen = pygame.display.set_mode((size_of_level, size_of_level))
    #Titre
    pygame.display.set_caption(window_title)
    fond = pygame.image.load(background).convert()
    victory_screen = pygame.image.load(victory).convert()
    screen.blit(fond, (0, 0))

    current_level.display_walls(screen)
    macgyver = Macgyver(0, 0, screen, current_level)
    macgyver.blit_mg()
    pygame.key.set_repeat(400, 30)

    active = 1
    gameplaying = 1
    #Loop for the game
    while active:

        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                active = 0      #stop the game
                gameplaying = 0
                
            if event.type == KEYDOWN:
                if event.key == K_F1:
                    #~ resetting position
                    macgyver = Macgyver(0, 0, screen, current_level)
                    gameplaying = 1

        while gameplaying : 
            for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
                if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                    active = 0 
                    gameplaying = 0     #On arrête la boucle

                if event.type == KEYDOWN:
                    if event.key == K_DOWN:
                        #~ move down
                        macgyver.move_mg('down')
                    if event.key == K_UP:
                        #~ move up
                        macgyver.move_mg('up')
                    if event.key == K_LEFT:
                        #~ move left
                        macgyver.move_mg('left')
                    if event.key == K_RIGHT:
                        #~ move right
                        macgyver.move_mg('right')
            screen.blit(fond, (0, 0))
            #~ print("Position : "+str(macgyver.sprite_x)+","+str(macgyver.sprite_y)).
            current_level.display_walls(screen)
            macgyver.blit_mg()
            if current_level.structure[macgyver.sprite_y][macgyver.sprite_x] == 'f':
                screen.blit(victory_screen, (0, 0))
                gameplaying = 0
            pygame.display.flip()




run_game()
