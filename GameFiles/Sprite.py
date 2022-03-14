"""
The Sprite.py file is used to create Sprites for the Freddy Takes on College game.
"""

import Settings
import pygame

class Sprite():
    # constructor
    def __init__(self, x, y, speed, imagePath, image_height=80, image_width=40):
        self.speed = speed
        #self.image = pygame.image.load(imagePath)
        #self.image = pygame.transform.scale(self.image, (image_width, image_height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    # setters
    def setX(self, x):
        self.rect.x = x

    def setY(self, y):
        self.rect.y = y

    def setSpeed(self, speed):
        self.speed = speed

    def changeImg(self, imagePath):
        self.image = pygame.image.load(imagePath)

    # getters
    def getX(self):
        return self.rect.x

    def getY(self):
        return self.rect.y

    def getSpeed(self):
        return self.speed

    # method to rotate Sprite image 
    def rotateImage(self, rotation):
        self.image = pygame.transform.rotate(self.image, rotation)

    # method to scale Sprite image
    def scaleImage(self, newWidth, newHeight):
        self.image = pygame.transform.scale(self.image, (newWidth, newHeight)) 