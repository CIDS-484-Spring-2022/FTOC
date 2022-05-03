"""
The file Exit.py holds the Exit class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player for the exit
doors. 
"""

import pygame

class Exit(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('GameFiles/Assets/door_openMid.png')
        self.image = pygame.transform.scale(image, (50, int(50 * 1.5))) # 50 is tile size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y