import pygame
import Settings
from Enemy import Enemy
from Lava import Lava

class Level():

    def __init__(self, level_data, tile_size, window):
        self.level_data = level_data
        self.tile_size = tile_size
        self.window = window
        self.tile_list = []
        self.enemy_group = pygame.sprite.Group()
        self.lava_group = pygame.sprite.Group()

        # load images (hard-coded for now but will change as we update the game)
        dirt_img = pygame.image.load('GameFiles/Assets/grassCenter.png')
        grass_img = pygame.image.load('GameFiles/Assets/grassMid.png')
        leftHalfGrass_img = pygame.image.load('GameFiles/Assets/grassHalfLeft.png')
        halfGrass_img = pygame.image.load('GameFiles/Assets/grassHalfMid.png')
        rightHalfGrass_img = pygame.image.load('GameFiles/Assets/grassHalfRight.png')
        halfStone_img = pygame.image.load('GameFiles/Assets/stoneHalfMid.png')
    
        #slime_img = pygame.image.load('GameFiles/Assets/slimeWalk1.png')

        # read level_data and put correct image and coordinates into a tile (temporarily hard-coded)
        row_num = 0
        for row in level_data:
            col_num = 0
            for tile in row:
                if tile == 1:
                    img = pygame.transform.scale(dirt_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 2:
                    img = pygame.transform.scale(grass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 3:
                    img = pygame.transform.scale(leftHalfGrass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 4:
                    img = pygame.transform.scale(halfGrass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 5:
                    img = pygame.transform.scale(rightHalfGrass_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 6:
                    img = pygame.transform.scale(halfStone_img, (tile_size, tile_size))
                    img_rect = img.get_rect()
                    img_rect.x = col_num * tile_size
                    img_rect.y = row_num * tile_size
                    tile = (img, img_rect)
                    self.tile_list.append(tile)
                if tile == 7:
                    lava = Lava(col_num * tile_size, row_num * tile_size + (tile_size // 2))
                    self.lava_group.add(lava)
                # Work in Progress
                if(tile == 10):
                    enemy = Enemy(col_num * tile_size, row_num * tile_size + 27)
                    self.enemy_group.add(enemy)
                


                col_num += 1
            row_num += 1
            
    def draw_level(self):
        for tile in self.tile_list:
            self.window.blit(tile[0], tile[1])
    
    def get_TileList(self) -> list:
        list = []
        for tile in self.tile_list:
            list.append(tile[0], tile[1])
        return list

    def get_EnemyGroup(self):
        return self.enemy_group

    def get_LavaGroup(self):
        return self.lava_group