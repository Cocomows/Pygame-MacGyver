"""Main module for macgyver game"""

import pygame
import random
from classes import *
from pygame.locals import *


def generate_collectables(current_level):
    """Place the character and all objects on the level"""
    list_of_collectables = []
    for i in range (0, number_of_collectables):
        #~ Randomly place the collectables on the available tiles.
        randTile = random.randint(0, len(current_level.available_tiles))
        collectable = Collectable(current_level.available_tiles[randTile], i)
        list_of_collectables.append(collectable)
        current_level.available_tiles.pop(randTile)
        #~ print(str(len(current_level.available_tiles)))
    
    return list_of_collectables


def run_game():
    """Main function for running the game"""
        

    #Initialisation de la bibliothèque Pygame
    pygame.init()
    pygame.display.set_caption(window_title)
    pygame.time.Clock().tick(30)
    pygame.key.set_repeat(100, 100)
    
    
    #~ Window creation
    screen = pygame.display.set_mode((size_of_level, size_of_level))
    
    victory_screen = pygame.image.load(victory).convert()
    lost_screen = pygame.image.load(lost).convert()
    
    #~ Get level structure in list
    current_level = Level('level')
    current_level.display_walls(screen)
    
    macgyver = Macgyver(0, 0, screen, current_level)
    list_of_collectables = generate_collectables(current_level)

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
                    #~ resetting game after victory or loss
                    current_level = Level('level') 
                    current_level.display_walls(screen)
                    macgyver = Macgyver(0, 0, screen, current_level)
                    list_of_collectables = generate_collectables(current_level)
                    gameplaying = 1

        while gameplaying:
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
            current_level.display_walls(screen)
            macgyver.blit_mg()
            
            
            #~ Check if an object is picked
            for collectable in list_of_collectables :
                if collectable.is_picked == False :
                    screen.blit(collectable.image, (collectable.posx, collectable.posy))
                
                if collectable.is_picked == False and macgyver.sprite_y == collectable.sprite_y and macgyver.sprite_x == collectable.sprite_x:
                    collectable.pick()
                    macgyver.items_collected += 1
                    #~ print("Object picked, items collected : "+str(macgyver.items_collected))
                
            #~ Check if character is on finish tile        
            if current_level.structure[macgyver.sprite_y][macgyver.sprite_x] == 'f' and macgyver.items_collected == number_of_collectables :
                screen.blit(victory_screen, (0, 0))
                gameplaying = 0
            elif current_level.structure[macgyver.sprite_y][macgyver.sprite_x] == 'f':
                screen.blit(lost_screen, (0, 0))
                gameplaying = 0

            #~ refresh screen
            pygame.display.flip()




run_game()
