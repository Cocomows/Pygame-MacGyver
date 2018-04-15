"""Main module for macgyver game"""

import pygame
from classes import *
from pygame.locals import *
 
    
def run_game():
    """Main function for running the game"""
    
    #~ Get level structure in list
    #~ current_level = generate_level()
    the_level = Level('level')
    
    #Initialisation de la bibliothèque Pygame
    pygame.init()

    #Création de la fenêtre
    screen = pygame.display.set_mode((size_of_level, size_of_level))
    fond = pygame.image.load(background).convert()
    screen.blit(fond, (0, 0))
   
    the_level.display_walls(screen)
    macgyver = Macgyver(0,0,screen)
    macgyver.blit_mg()

    active = 1

    #Loop for the game
    while active:
        for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
            if event.type == QUIT:     #Si un de ces événements est de type QUIT
                active = 0      #On arrête la boucle
   
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
        print("Position : "+str(macgyver.sprite_x)+","+str(macgyver.sprite_y))
        the_level.display_walls(screen)
        macgyver.blit_mg()
        pygame.display.flip()




run_game()
