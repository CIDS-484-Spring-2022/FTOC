"""
The Sprite.py file is used to create Sprites for the Freddy Takes on College game.
"""

import Settings
import pygame

class Sprite():
    # constructor
    def __init__(self, x, y, speed, imagePath):
        self.x = x
        self.y = y
        self.speed = speed
        self.image = pygame.image.load(imagePath)

    # setters
    def setX(self, x):
        self.x = x

    def setY(self, y):
        self.y = y

    def setSpeed(self, speed):
        self.speed = speed

    # getters
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getSpeed(self):
        return self.speed

    # method to rotate Sprite image 
    def rotateImage(self, rotation):
        self.image = pygame.transform.rotate(self.image, rotation)

    # method to scale Sprite image
    def scaleImage(self, newWidth, newHeight):
        self.image = pygame.transform.scale(self.image, (newWidth, newHeight)) 