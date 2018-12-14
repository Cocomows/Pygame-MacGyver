#! /usr/bin/env python3
# coding: utf-8
"""Constants for the macgyver game"""

# Window parameters
SPRITES_IN_LEVEL = 15
SIZE_OF_SPRITE = 30
SIZE_OF_LEVEL = SPRITES_IN_LEVEL * SIZE_OF_SPRITE

# List of pictures in the game
BACKGROUND = 'images/fond.jpg'
WALLPIC = 'images/mur.png'
MACGYVERPIC = 'images/macgyver.png'
GUARDIANPIC = 'images/guardian.png'
VICTORY = 'images/victory.jpg'
LOST = 'images/lost.jpg'
OBJECTS_IMAGES = ['images/needle.png', 'images/tube.png', 'images/ether.png',]


# Game parameters
NUMBER_OF_COLLECTABLES = len(OBJECTS_IMAGES)


# Window parameters
WINDOW_TITLE = "MacGyver"
