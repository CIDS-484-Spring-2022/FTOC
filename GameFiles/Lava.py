"""
The file Lava.py holds the Lava class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player. 
"""

import pygame
import Settings

class Lava(pygame.sprite.Sprite):

    # constructor
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('GameFiles/Assets/liquidLavaTop_mid.png')
        self.image = pygame.transform.scale(image, (Settings.TILE_SIZE, Settings.TILE_SIZE // 2))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        