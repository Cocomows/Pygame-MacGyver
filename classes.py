"""file with all classes for the macgyver game"""
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
        self.image = pygame.image.load(macgyverpic).convert_alpha()

    def blit_mg(self):
        """display character on the screen"""
        self.screen.blit(self.image, (self.posx, self.posy))

    def move_mg(self, direction):
        "move character in the proper direction"""
        if direction == 'down':
            if self.sprite_y < (sprites_in_level-1):
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
            if self.sprite_x < (sprites_in_level-1):
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

    def generate_level(self):
        """Generates the level as a table from file 'level', returns the table"""
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
        """Reads the level table and returns all non-wall tiles"""

        
        wall = pygame.image.load(wallpic).convert_alpha()
        guardian = pygame.image.load(guardianpic).convert_alpha()

        num_line = 0
        for ligne_horiz in self.structure:
            num_col = 0
            for ligne_vert in ligne_horiz:

                position_x = num_col * size_of_sprite

                position_y = num_line * size_of_sprite

                if ligne_vert == str(1):
                    screen.blit(wall, (position_x, position_y))
                elif ligne_vert == 'f':
                    screen.blit(guardian, (position_x,position_y))
                else:
                    if ligne_vert == str(0):
                        self.available_tiles.append((num_line, num_col))

                num_col += 1
            num_line += 1
        #~ print("Liste des cases disponibles : "+str(case_dispo))




