"""
The file Lava.py holds the Lava class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player. 
"""

import pygame

class Lava(pygame.sprite.Sprite):

    # constructor
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('GameFiles/Assets/liquidLavaTop_mid.png')
        self.image = pygame.transform.scale(image, (50, 50 // 2)) # 50 is tile size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        