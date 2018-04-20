#! /usr/bin/env python3
# coding: utf-8
"""Main module for macgyver game"""

import random
import pygame

from classes import *
from pygame.locals import QUIT, KEYDOWN, K_F1, K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE


def generate_collectables(current_level):
    """Place the character and all objects on the level"""
    list_of_collectables = []
    for i in range(0, number_of_collectables):
        #~ Randomly place the collectables on the available tiles.
        rand_tile = random.randint(0, len(current_level.available_tiles)-1)
        collectable = Collectable(current_level.available_tiles[rand_tile], i)
        list_of_collectables.append(collectable)
        current_level.available_tiles.pop(rand_tile)
    return list_of_collectables

def play_the_game(macgyver, list_of_collectables, screen, current_level, active, gameplaying):
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
    for collectable in list_of_collectables:
        if collectable.is_picked is False:
            screen.blit(collectable.image, (collectable.posx, collectable.posy))

        if collectable.is_picked is False and macgyver.sprite_y == collectable.sprite_y \
            and macgyver.sprite_x == collectable.sprite_x:
            collectable.is_picked = True
            macgyver.items_collected += 1
            #~ print("Object picked, items collected : "+str(macgyver.items_collected))


    macgyver.blit_mg()


    return active, gameplaying

def collection_complete(macgyver):
    """Returns true if all objects are collected"""
    return macgyver.items_collected == number_of_collectables

def finish_tile_reached(current_level, macgyver):
    """Returns true when character is on finish tile"""
    return current_level.structure[macgyver.sprite_y][macgyver.sprite_x] == 'f'

def set_game():
    """Set the parameters for the game"""
    #~ Window creation
    screen = pygame.display.set_mode((size_of_level, size_of_level))

    #~ Get level structure in list
    current_level = Level('level')
    current_level.display_walls(screen)

    macgyver = Macgyver(0, 0, screen, current_level)
    list_of_collectables = generate_collectables(current_level)

    active = 1
    gameplaying = 1
    return (macgyver, list_of_collectables, screen, current_level, active, gameplaying)

def main():
    """Main function for running the game"""


    #~ Pygame initialisation
    pygame.init()
    pygame.display.set_caption(window_title)
    pygame.time.Clock().tick(100)
    pygame.key.set_repeat(100, 100)

    #~ Set the game
    macgyver, list_of_collectables, screen, current_level, active, gameplaying = set_game()
    victory_screen = pygame.image.load(victory).convert()
    lost_screen = pygame.image.load(lost).convert()

    #~ Loop for the game
    while active:

        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                active = 0      #stop the game
                gameplaying = 0

            if event.type == KEYDOWN:
                if event.key == K_F1:
                    #~ Reset the game
                    macgyver, list_of_collectables, screen, current_level, active, gameplaying = set_game()

        while gameplaying:

            active, gameplaying = play_the_game(macgyver, list_of_collectables, screen, current_level, active, gameplaying)

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
