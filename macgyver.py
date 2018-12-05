#! /usr/bin/env python3
# coding: utf-8
"""Main module for macgyver game"""

import pygame
from maze import Maze
from pygame.locals import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE
from classes import *


def play_the_game(macgyver, screen, current_level, active, gameplaying):
    """Main actions of playing including moving and collecting items"""

    current_level.display_walls(screen)
    #~ Check if an event making the character move happens and make the character move
    for event in pygame.event.get():
        if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
            active = 0
            gameplaying = 0
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

    #~ Check if an object is picked
    for collectable in current_level.list_of_collectables:
        if not collectable.is_picked:
            screen.blit(collectable.image, (collectable.posx, collectable.posy))

        if (not collectable.is_picked and macgyver.sprite_y == collectable.sprite_y and
                macgyver.sprite_x == collectable.sprite_x):
            collectable.is_picked = True
            macgyver.items_collected += 1

    macgyver.blit_mg()

    return active, gameplaying

def collection_complete(macgyver):
    """Returns true if all objects are collected"""
    return macgyver.items_collected == NUMBER_OF_COLLECTABLES

def finish_tile_reached(current_level, macgyver):
    """Returns true when character is on finish tile"""
    return current_level.structure[macgyver.sprite_y][macgyver.sprite_x] == 'f'

def set_game():
    """Set the parameters for the game"""
    #~ Window creation
    screen = pygame.display.set_mode((SIZE_OF_LEVEL, SIZE_OF_LEVEL))

    #~ Get level structure in list
    mymaze = Maze()

    current_level = Level('level_')
    current_level.display_walls(screen)
    current_level.generate_collectables()

    macgyver = Macgyver(0, 0, screen, current_level)

    active = 1
    gameplaying = 1
    return (macgyver, screen, current_level, active, gameplaying)

def main():
    """Main function for running the game"""


    #~ Pygame initialisation
    pygame.init()
    pygame.display.set_caption(WINDOW_TITLE)
    pygame.time.Clock().tick(100)
    pygame.key.set_repeat(100, 100)

    #~ Set the game
    macgyver, screen, current_level, active, gameplaying = set_game()
    victory_screen = pygame.image.load(VICTORY).convert()
    lost_screen = pygame.image.load(LOST).convert()

    #~ Loop for the game
    while active:

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                #~ Stop the game
                active = 0
                gameplaying = 0

            if event.type == KEYDOWN:
                if event.key == K_F1:
                    #~ Reset the game
                    (macgyver, screen, current_level,
                     active, gameplaying) = set_game()

        while gameplaying:

            active, gameplaying = play_the_game(macgyver, screen, current_level,
                                                active, gameplaying)

            #~ When the finish tile is reached, display win or lose screen
            if finish_tile_reached(current_level, macgyver):
                gameplaying = 0
                if collection_complete(macgyver):
                    screen.blit(victory_screen, (0, 0))
                else:
                    screen.blit(lost_screen, (0, 0))

            #~ refresh screen
            pygame.display.flip()



if __name__ == "__main__":
    main()
