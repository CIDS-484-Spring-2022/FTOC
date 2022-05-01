import Settings
import pygame
from Sprite import Sprite
from Level import Level

# the Player class inherits from the Sprite class
class Player(Sprite):

    # constructor
    # instead of image path do character name and then do it that way so you load all the images and animation images
    # hard-coded for now but will change as this was temporary to figure out the correct logic
    def __init__(self, x, y, speed, imagePath, characterName, image_height=80, image_width=40):
        self.images_right = [] 
        self.images_left = []
        self.index = 0 
        self.counter = 0

        for num in range(0, 8):
            img = pygame.image.load(f'GameFiles/Assets/character_maleAdventurer_walk{num}.png')
            img_right = pygame.transform.scale(img, (image_width, image_height))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        self.idle_image = pygame.image.load('GameFiles/Assets/character_maleAdventurer_idle.png')
        self.idle_image = pygame.transform.scale(self.idle_image, (image_width, image_height))

        self.jump_right = pygame.image.load('GameFiles/Assets/character_maleAdventurer_jump.png')
        self.jump_right = pygame.transform.scale(self.jump_right, (image_width, image_height))
        self.jump_left = pygame.transform.flip(self.jump_right, True, False)

        self.fall_right = pygame.image.load('GameFiles/Assets/character_maleAdventurer_fall.png')
        self.fall_right = pygame.transform.scale(self.fall_right, (image_width, image_height))
        self.fall_left = pygame.transform.flip(self.fall_right, True, False) 

        self.image = self.idle_image
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        super().__init__(x, y, speed, imagePath)
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0
        self.jumping = False
        self.direction = 0 # positive value means moving right while negative means left
    
    def update(self, window, level: Level):
        # local variables
        dx = 0
        dy = 0 
        walking_cooldown = 5

        # get key presses
        key = pygame.key.get_pressed()

        # handle jumping
        if key[pygame.K_SPACE] and self.jumping == False:
            self.vel_y = -15
            self.jumping = True

        if key[pygame.K_SPACE] == False:
            self.jumping = False

        # handle moving left
        if key[pygame.K_LEFT]:
            dx -= 5
            self.counter += 1
            self.direction = -1

        # handle moving right
        if key[pygame.K_RIGHT]:
            dx += 5
            self.counter += 1
            self.direction = 1
        
        # handle no movement
        if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False and key[pygame.K_SPACE] == False:
            self.counter = 0
            self.index = 0
            if self.direction == 1:
                self.image = self.idle_image
            if self.direction == -1:
                self.image = pygame.transform.flip(self.idle_image, True, False)

        # left and right animation handler
        if self.counter > walking_cooldown:
            self.counter = 0
            self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:  
                self.image = self.images_right[self.index]
            if self.direction == -1:  
                self.image = self.images_left[self.index]

        # account for gravity 
        self.vel_y += 1
        if self.vel_y > 10:
            self.vel_y = 10
        dy += self.vel_y

        # up animation handler
        if dy < 0 and (self.direction == 1 or self.direction == 0):
            self.image = self.jump_right
        if dy < 0 and self.direction == -1:
            self.image = self.jump_left

        # check for collision
        tile_list = level.tile_list
        for tile in level.tile_list:
            # check for collison in x direction
            if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                dx = 0

            # check for collision in y direction
            if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                # check if jumping (i.e. below ground)
                if self.vel_y < 0:
                    dy = tile[1].bottom - self.rect.top
                    self.vel_y = 0
                # check if falling (i.e. above ground)
                elif self.vel_y >= 0:
                    dy = tile[1].top - self.rect.bottom
                    self.vel_y = 0
            
        # update coordinates
        self.rect.x += dx
        self.rect.y += dy

        # temporary
        if self.rect.bottom > Settings.WINDOW_HEIGHT:
            self.rect.bottom = Settings.WINDOW_HEIGHT
            dy = 0

        # handle falling back onto the ground after jumping
        if dy == 0 and (self.direction == 1 or self.direction == 0) and self.jumping == True:
                self.image = self.idle_image
        if dy == 0 and self.direction == -1 and self.jumping == True:
            self.image = pygame.transform.flip(self.idle_image, True, False)

        # draw player on screen
        window.blit(self.image, self.rect)
