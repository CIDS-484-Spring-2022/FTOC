"""
The file Player.py represents the character that the user will control during the game. It handles loading in various images
that are used for the player as well as drawing the player onto the screen. Also, it handles collision between tiles and other 
elements the user may interact with. Also, there are methods to handle user input for moving the player around the levels
"""

from cgitb import reset
import Settings
import pygame
from Level import Level

class Player():

    # constructor
    def __init__(self, x, y, jump_fx):
        self.reset(x, y, image_height=80, image_width=40)
        self.jump_fx = jump_fx
        
    # Method to set the current level the player is on
    def update_CurrentLevel(self, level: Level):
        self.currentLevel = level

    # Method to update number of deaths
    def update_Deaths(self, update):
        if update == 1:
            Settings.NUM_DEATHS += 1
        else:
            Settings.NUM_DEATHS = 0

    # method that updates the player as the user interacts with the level
    def update(self, window, level: Level):
        # local variables
        dx = 0
        dy = 0 
        walking_cooldown = 5
        collision_threshold = 20

        if Settings.GAME_OVER == 0:
            # get key presses
            key = pygame.key.get_pressed()

            # handle jumping
            if key[pygame.K_SPACE] and self.jumping == False and self.in_air == False:
                self.jump_fx.play()
                self.vel_y = -15
                self.jumping = True

            if key[pygame.K_SPACE] == False:
                self.jumping = False
                #self.image = self.idle_image

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
            self.in_air = True
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
                        self.in_air = False

            # check for enemy collision
            if pygame.sprite.spritecollide(self, Level.get_EnemyGroup(self.currentLevel), False):
                self.update_Deaths(1)
                Settings.GAME_OVER = -1

            # check for exit collision 
            if pygame.sprite.spritecollide(self, Level.get_ExitGroup(self.currentLevel), False):
                Settings.GAME_OVER = 1 # positive means level is won

            # check for lava collision 
            if pygame.sprite.spritecollide(self, Level.get_LavaGroup(self.currentLevel), False):
                self.update_Deaths(1)
                Settings.GAME_OVER = -1

            # check for moving platform collision
            for platform in Level.get_PlatformGroup(self.currentLevel):
                
                # collision in x direction
                if platform.rect.colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx = 0

                # collision in y direction
                if platform.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):

                    # check if below platform
                    if abs((self.rect.top + dy) - platform.rect.bottom) < collision_threshold:
                        self.vel_y = 0
                        dy = platform.rect.bottom - self.rect.top

                    # check if above platform
                    elif abs((self.rect.bottom + dy) - platform.rect.top) < collision_threshold:
                        self.rect.bottom = platform.rect.top - 1
                        self.in_air = False
                        dy = 0
                    
                    # move sideways with the platform
                    if platform.move_x != 0:
                        self.rect.x += platform.move_direction

            # down animation handler
            if dy > 0 and (self.direction == 1 or self.direction == 0) and self.in_air == True:
                self.image = self.fall_right
            if dy > 0 and self.direction == -1 and self.in_air == True:
                self.image = self.fall_left

            # update coordinates
            self.rect.x += dx
            self.rect.y += dy

            # handle falling back onto the ground after jumping
            if dy == 0 and (self.direction == 1 or self.direction == 0) and self.jumping == True:
                self.image = self.idle_image
            if dy == 0 and self.direction == -1 and self.jumping == True:
                self.image = pygame.transform.flip(self.idle_image, True, False)

        elif Settings.GAME_OVER == -1:
            self.image = self.dead_image

            if self.rect.y > 200:
                self.rect.y -= 5
            elif self.rect.y <= 200:
                Settings.GAME_OVER = 0
                self.reset(100, Settings.WINDOW_HEIGHT-130)

        # draw player on screen
        window.blit(self.image, self.rect)
        #pygame.draw.rect(window, (255, 255, 255), self.rect, 2)

    def reset(self, x, y, image_height=80, image_width=40):
        # variables used in player animation
        self.images_right = [] 
        self.images_left = []
        self.index = 0 
        self.counter = 0

        # load in the images for when the player is walking
        for num in range(0, 8):
            img = pygame.image.load(f'GameFiles/Assets/character_femaleAdventurer_walk{num}.png')
            img_right = pygame.transform.scale(img, (image_width, image_height))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)

        # load image for when playet dies
        self.dead_image = pygame.image.load("GameFiles/Assets/ghost.png")

        # load image for when the player is idle
        self.idle_image = pygame.image.load('GameFiles/Assets/character_femaleAdventurer_idle.png')
        self.idle_image = pygame.transform.scale(self.idle_image, (image_width, image_height))

        # load image for when the player jumps
        self.jump_right = pygame.image.load('GameFiles/Assets/character_femaleAdventurer_jump.png')
        self.jump_right = pygame.transform.scale(self.jump_right, (image_width, image_height))
        self.jump_left = pygame.transform.flip(self.jump_right, True, False)

        self.fall_right = pygame.image.load('GameFiles/Assets/character_femaleAdventurer_fall.png')
        self.fall_right = pygame.transform.scale(self.fall_right, (image_width, image_height))
        self.fall_left = pygame.transform.flip(self.fall_right, True, False) 

        # set starter image to idle
        self.image = self.idle_image

        # create a rectangle around the player for use in collision detection
        self.rect = self.image.get_rect()
        self.width = self.image.get_width()
        self.height = self.image.get_height() 
        #super().__init__(x, y, speed, imagePath)
        self.rect.x = x
        self.rect.y = y
        self.vel_y = 0

        # variables to detect whether the player is jumping or in the air
        self.jumping = False
        self.in_air = True

        # variable that represents which direction the player is moving (positive value means moving right while negative means left)
        self.direction = 1 