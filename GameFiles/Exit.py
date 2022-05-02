from tkinter import image_types
import pygame

class Exit(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        image = pygame.image.load('GameFiles/Assets/door_openMid.png')
        self.image = pygame.transform.scale(image, (50, int(50 * 1.5))) # 50 is tile size
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y