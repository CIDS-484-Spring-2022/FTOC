from tkinter import image_types
import Settings
import pygame

# WORK IN PROGRESS

class Enemy(pygame.sprite.Sprite):
    
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('GameFiles/Assets/slimeWalk1.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        