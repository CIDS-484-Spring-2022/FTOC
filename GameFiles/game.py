"""
The game.py file contains methods that create the game and updates the screen.  
"""

from re import S
import pygame
from pygame import mixer
import Settings
from menu import *
import Level_Data
from Level import Level
from Player import Player

mAdventurerPath = ""

WIN = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
pygame.display.set_caption("Lost in the Mountains!")



class Game():
    def __init__(self):
        pygame.init()
        pygame.mixer.pre_init(44100, -16, 2, 512)
        mixer.init()

        # Neverland by Alexander Nakarada | https://www.serpentsoundstudios.com
        # Music promoted by https://www.chosic.com/free-music/all/
        # Creative Commons CC BY 4.0
        # https://creativecommons.org/licenses/by/4.0/
        pygame.mixer.music.load('GameFiles/Assets/Neverland.wav')
        pygame.mixer.music.play(-1, 0.0, 5000)

        # Sound from zapsplat.com
        self.jump_fx = pygame.mixer.Sound('GameFiles/Assets/jump_fx.wav')
        self.jump_fx.set_volume(0.50)
        
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY, self.ESCAPE_KEY = False, False, False, False, False
        self.display = pygame.Surface((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
        self.window = pygame.display.set_mode(((Settings.WINDOW_WIDTH,Settings.WINDOW_HEIGHT)))
        self.font_name = pygame.font.Font("GameFiles/Assets/ARCADECLASSIC.TTF", 16)
        self.WHITE, self.BLACK, self.RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
        self.main_menu = MainMenu(self)
        self.options = ControlsMenu(self)
        self.levels = LevelSelection(self)
        self.curr_menu = self.main_menu

    def draw_grid():
        for line in range(0, (int(Settings.WINDOW_HEIGHT/Settings.TILE_SIZE))):
            pygame.draw.line(WIN, (255, 255, 255), (0, line * Settings.TILE_SIZE), (Settings.WINDOW_WIDTH, line * Settings.TILE_SIZE))
        for line in range(0, (int(Settings.WINDOW_WIDTH/Settings.TILE_SIZE))):
            pygame.draw.line(WIN, (255, 255, 255), (line * Settings.TILE_SIZE, 0), (line * Settings.TILE_SIZE, Settings.WINDOW_HEIGHT))

    def game_loop(self):

        clock = pygame.time.Clock()
        self.playing = True

        self.num_deaths = 0
    
        player = Player(100, Settings.WINDOW_HEIGHT-130, self.jump_fx)
        level_1 = Level(Level_Data.level1, Settings.TILE_SIZE, WIN)
        level_2 = Level(Level_Data.level2, Settings.TILE_SIZE, WIN)
        level_3 = Level(Level_Data.level3, Settings.TILE_SIZE, WIN)
        level_4 = Level(Level_Data.level4, Settings.TILE_SIZE, WIN)
        level_5 = Level(Level_Data.level5, Settings.TILE_SIZE, WIN)
        level_6 = Level(Level_Data.level6, Settings.TILE_SIZE, WIN)
        level_7 = Level(Level_Data.level7, Settings.TILE_SIZE, WIN)
        level_8 = Level(Level_Data.level8, Settings.TILE_SIZE, WIN)

        while self.playing:

            if self.levels.state == 'Level1':
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_1.draw_level()
                player.update_CurrentLevel(level_1)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_1)

                if Settings.GAME_OVER == 0:                
                    enemy_group.update()
                    
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_1)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_1).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_1).draw(WIN)

                player.update(WIN, level_1) 

                self.check_events()

                pygame.display.update()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level2'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

            elif self.levels.state == 'Level2':        

                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_2.draw_level()
                player.update_CurrentLevel(level_2)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_2)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_2)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_2).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_2).draw(WIN)

                player.update(WIN, level_2) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level3'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()

            elif self.levels.state == 'Level3':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_3.draw_level()
                player.update_CurrentLevel(level_3)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_3)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_3)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_3).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_3).draw(WIN)

                player.update(WIN, level_3) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level4'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()

            elif self.levels.state == 'Level4':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_4.draw_level()
                player.update_CurrentLevel(level_4)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_4)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_4)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_4).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_4).draw(WIN)

                player.update(WIN, level_4) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level5'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()
            elif self.levels.state == 'Level5':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_5.draw_level()
                player.update_CurrentLevel(level_5)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_5)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_5)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_5).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_5).draw(WIN)

                player.update(WIN, level_5) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level6'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()
            elif self.levels.state == 'Level6':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_6.draw_level()
                player.update_CurrentLevel(level_6)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_6)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_6)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_6).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_6).draw(WIN)

                player.update(WIN, level_6) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level7'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()
            elif self.levels.state == 'Level7':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_7.draw_level()
                player.update_CurrentLevel(level_7)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_7)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_7)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_7).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_7).draw(WIN)

                player.update(WIN, level_7) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                if Settings.GAME_OVER == 1:
                    self.levels.state = 'Level8'
                    player.reset(100, Settings.WINDOW_HEIGHT-130)
                    Settings.GAME_OVER = 0

                pygame.display.update()
            elif self.levels.state == 'Level8':        
                clock.tick(Settings.FPS)

                WIN.blit(Settings.GAME_BG, (0, 0))
                #draw_grid()
                level_8.draw_level()
                player.update_CurrentLevel(level_8)

                # ENEMIES
                enemy_group = Level.get_EnemyGroup(level_8)
                enemy_group.update()
                enemy_group.draw(WIN)

                # Moving Platforms
                platform_group = Level.get_PlatformGroup(level_8)
                platform_group.update()
                platform_group.draw(WIN)

                # LAVA
                Level.get_LavaGroup(level_8).draw(WIN)

                # Death counter
                self.draw_DeathCounter('X ' + str(Settings.NUM_DEATHS), Settings.TILE_SIZE - 10, 5)
                ghost_score = pygame.image.load("GameFiles/Assets/deathCounterIcon3.png")
                ghost_score = pygame.transform.scale(ghost_score, (int(Settings.TILE_SIZE // 1.5), int(Settings.TILE_SIZE // 1.5)))
                WIN.blit(ghost_score, (3, 5))

                # EXIT
                Level.get_ExitGroup(level_8).draw(WIN)

                player.update(WIN, level_8) 

                self.check_events()

                if self.BACK_KEY == True:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False 

                # When last level is complete, go to the menu and reset the death counter
                if Settings.GAME_OVER == 1:
                    self.curr_menu.display_menu()
                    self.playing = False
                    self.levels.start = False
                    player.update_Deaths(0)

                pygame.display.update()

            pygame.display.update()


        #pygame.quit()
    
        #self.curr_menu.display_menu()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.K_ESCAPE:
                self.ESCAPE_KEY = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font("GameFiles/Assets/ARCADECLASSIC.TTF", size)
        text_surface = font.render(text, True, self.BLACK)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

    def draw_DeathCounter(self, text, x, y):
        font = pygame.font.Font("GameFiles/Assets/ARCADECLASSIC.TTF", 40)
        img = font.render(text, True, self.WHITE)
        WIN.blit(img, (x, y))

