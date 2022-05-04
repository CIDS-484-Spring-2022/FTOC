"""
The file Exit.py holds the Exit class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player for the exit
doors. 
"""

import pygame
import Settings

class Exit(pygame.sprite.Sprite):

    def __init__(self, x, y, exit_top):
        pygame.sprite.Sprite.__init__(self)

        if(exit_top == 0):
            image = pygame.image.load('GameFiles/Assets/door_openMid.png')
        else:
            image = pygame.image.load('GameFiles/Assets/door_openTop.png')
        self.image = pygame.transform.scale(image, (Settings.TILE_SIZE, int(Settings.TILE_SIZE * 1.5))) 
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y