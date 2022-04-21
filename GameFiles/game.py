from re import S
import pygame
import Settings
from menu import *
import Level_Data
from Level import Level
from Player import Player

mAdventurerPath = ""
BG_IMAGE = pygame.image.load('GameFiles/Assets/GreenHillsBG.png')
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

tile_size = 50

WIN = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
pygame.display.set_caption("Freddy Takes on College!")





class Game():
    def __init__(self):
        pygame.init()
        self.running = True
        self.playing = False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.display = pygame.Surface((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
        self.window = pygame.display.set_mode(((Settings.WINDOW_WIDTH,Settings.WINDOW_HEIGHT)))
        self.font_name = pygame.font.Font("GameFiles/Assets/ARCADECLASSIC.TTF", 16)
        self.WHITE, self.BLACK, self.RED = (255, 255, 255), (0, 0, 0), (255, 0, 0)
        self.main_menu = MainMenu(self)
        self.options = ControlsMenu(self)
        self.levels = LevelSelection(self)
        self.curr_menu = self.main_menu

    def draw_grid():
        for line in range(0, (int(Settings.WINDOW_HEIGHT/tile_size))):
            pygame.draw.line(WIN, (255, 255, 255), (0, line * tile_size), (Settings.WINDOW_WIDTH, line * tile_size))
        for line in range(0, (int(Settings.WINDOW_WIDTH/tile_size))):
            pygame.draw.line(WIN, (255, 255, 255), (line * tile_size, 0), (line * tile_size, Settings.WINDOW_HEIGHT))

    def game_loop(self):

        # GUI/Game code to go here
        clock = pygame.time.Clock()
        run = True
    
        player = Player(100, Settings.WINDOW_HEIGHT-130, 5, 'GameFiles/Assets/character_maleAdventurer_idle.png', 'maleAdventurer')
        level_1 = Level(Level_Data.level1, tile_size, WIN)
        level_2 = Level(Level_Data.level2, tile_size, WIN)


        print(self.levels.state)

        if self.levels.state == 'Level1':

            while run:
                clock.tick(Settings.FPS)

                WIN.blit(BG_IMAGE, (0, 0))
                #draw_grid()
                level_1.draw_level()
                player.update(WIN, level_1) # hard-coded for now

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                pygame.display.update()

        elif self.levels.state == 'Level2':        
            while run:
                clock.tick(Settings.FPS)

                WIN.blit(BG_IMAGE, (0, 0))
                #draw_grid()
                level_2.draw_level()
                player.update(WIN, level_2) # hard-coded for now

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                pygame.display.update()

        pygame.quit()

    """
        while self.playing:
            self.check_events()
            #this is where you would add our game levels
            self.window.blit(self.display, (0,0))
            pygame.display.update()
            self.reset_keys()
    """

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
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
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)

