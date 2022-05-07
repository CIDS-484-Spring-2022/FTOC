"""
The Settings.py file contains some common constants that will be used in the 'Lost in the Mountains' Game
"""

import pygame
from pygame import mixer

WINDOW_HEIGHT = 750
WINDOW_WIDTH = 1000

FPS = 60

GAME_OVER = 0

TILE_SIZE = 50

GAME_BG = pygame.transform.scale(pygame.image.load('GameFiles/Assets/GreenHillsBG.png'), (WINDOW_WIDTH, WINDOW_HEIGHT))

MENU_BG = pygame.transform.scale(pygame.image.load('GameFiles/Assets/menuBackground.png'), (WINDOW_WIDTH, WINDOW_HEIGHT))

NUM_DEATHS = 0