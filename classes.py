#! /usr/bin/env python3
# coding: utf-8
"""file with all classes for the macgyver game"""
import random
import pygame
from constants import *

class Macgyver:
    """ class representing the character played"""

    def __init__(self, x, y, screen, level):
        self.posx = x
        self.posy = y
        self.sprite_x = int(x / 30)
        self.sprite_y = int(y / 30)
        self.level = level
        self.screen = screen
        self.image = pygame.image.load(MACGYVERPIC).convert_alpha()
        self.items_collected = 0

    def blit_mg(self):
        """display character on the screen"""
        self.screen.blit(self.image, (self.posx, self.posy))

    def move_mg(self, direction):
        "move character in the proper direction"""
        if direction == 'down':
            if self.sprite_y < (SPRITES_IN_LEVEL-1):
                if self.level.structure[self.sprite_y+1][self.sprite_x] != '1':
                    self.posy += 30
                    self.sprite_y += 1

        elif direction == 'up':
            if self.sprite_y > 0:
                if self.level.structure[self.sprite_y-1][self.sprite_x] != '1':
                    self.posy -= 30
                    self.sprite_y -= 1

        elif direction == 'left':
            if self.sprite_x > 0:
                if self.level.structure[self.sprite_y][self.sprite_x-1] != '1':
                    self.posx -= 30
                    self.sprite_x -= 1

        elif direction == 'right':
            if self.sprite_x < (SPRITES_IN_LEVEL-1):
                if self.level.structure[self.sprite_y][self.sprite_x+1] != '1':
                    self.posx += 30
                    self.sprite_x += 1


class Level:
    """ class representing the level of the game"""

    def __init__(self, level_file):

        self.level_file = level_file
        self.structure = []
        self.generate_level()
        self.available_tiles = []
        self.fond = pygame.image.load(BACKGROUND).convert()
        self.list_of_collectables = []

    def generate_level(self):
        """Generates the level as a table from file 'level' """
        with open(self.level_file, "r") as level_file:
            level_list = []
            for line in level_file:
                line_list = []
                for char in line:
                    if char != '\n':
                        line_list.append(char)
                level_list.append(line_list)
        self.structure = level_list

    def display_walls(self, screen):
        """Reads the level table, displays walls and guardian
        and stores all non-wall tiles in available_tiles"""


        wall = pygame.image.load(WALLPIC).convert_alpha()
        guardian = pygame.image.load(GUARDIANPIC).convert_alpha()

        screen.blit(self.fond, (0, 0))

        num_line = 0
        for ligne_horiz in self.structure:
            num_col = 0
            for ligne_vert in ligne_horiz:

                position_x = num_col * SIZE_OF_SPRITE

                position_y = num_line * SIZE_OF_SPRITE

                if ligne_vert == str(1):
                    screen.blit(wall, (position_x, position_y))
                elif ligne_vert == 'f':
                    screen.blit(guardian, (position_x, position_y))
                else:
                    if ligne_vert == str(0):
                        self.available_tiles.append((num_col, num_line))

                num_col += 1
            num_line += 1

    def generate_collectables(self):
        """Place the collectable objects on the level"""

        for i in range(0, NUMBER_OF_COLLECTABLES):
            #~ Randomly place the collectables on the available tiles.
            rand_tile = random.randint(0, len(self.available_tiles)-1)
            collectable = Collectable(self.available_tiles[rand_tile], i)
            self.list_of_collectables.append(collectable)
            self.available_tiles.pop(rand_tile)



class Collectable:
    """Represents objects player has to collect"""
    def __init__(self, coordinates, style):

        self.sprite_x = coordinates[0]
        self.sprite_y = coordinates[1]
        self.posx = self.sprite_x * 30
        self.posy = self.sprite_y * 30
        self.style = style
        self.is_picked = False
        self.image = pygame.image.load(OBJECTS_IMAGES[style]).convert_alpha()


