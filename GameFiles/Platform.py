"""
The file Platform.py holds the Platform class for the 'Lost in the Mountains' game. This class is responsible for setting the image, 
scaling the image, and creating a rectangle with x and y values to be used in collision detection with the player for the moving 
platforms. Also, contains a function to control which way the platform moves.
"""

import pygame

class Platform(pygame.sprite.Sprite):

    # constructor
    def __init__(self, x, y, move_x, move_y):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('GameFiles/Assets/grassHalf.png')
        self.image = pygame.transform.scale(image, (50, 50)) # 50 is tile size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        # variables that are used to control platform move direction
        self.move_counter = 0
        self.move_direction = 1

        # variables to differentiate the two types of platforms
        self.move_x = move_x
        self.move_y = move_y

    # method to handle platform movement
    def update(self):

        # handles movement for the platform
        self.rect.x += self.move_direction * self.move_x
        self.rect.y += self.move_direction * self.move_y
        self.move_counter += 1

        # allows for the platforms to move both ways in their respective directions (ex. up and down or left and right)
        if abs(self.move_counter) > 50:
            self.move_direction *= -1
            self.move_counter *= -1 