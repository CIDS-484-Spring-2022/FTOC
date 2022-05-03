"""
The file Enemy.py holds the Enemy class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player for the slime
enemy. Also, contains a function to control enemy movement.
"""

import pygame

class Enemy(pygame.sprite.Sprite):
    
    # constructor
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('GameFiles/Assets/blockerMad.png')
        self.image = pygame.transform.scale(self.image, (25, 25))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        # variables that is used to control which way the enemy is moving
        self.move_direction = 1
        self.move_counter = 0

    # method for handing the movement of the enemy
    def update(self):
        # move the enemy
        self.rect.x += self.move_direction
        self.move_counter += 1

        # allow for the enemy to move back and forth
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1