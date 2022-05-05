import pygame
import Settings

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('[', 30, self.cursor_rect.x + self.offset, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Levels"
        self.levelsx, self.levelsy = self.mid_w, self.mid_h + 20
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 80
        self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
        pygame.display.set_caption("Lost in the Mountains")


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            #self.menuBG = pygame.image.load('GameFiles/Assets/menuBackground.png')
            #self.menuBG = pygame.transform.scale(self.menuBG, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
            #self.game.display.fill(self.game.BLACK)
            self.game.display.blit(Settings.MENU_BG, (0, 0))
            self.game.draw_text("Level Selection", 50, self.levelsx, self.levelsy)
            self.game.draw_text("Controls", 50, self.optionsx, self.optionsy)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Levels':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'
        elif self.game.UP_KEY:
            if self.state == 'Levels':
                self.cursor_rect.midtop = (self.optionsx + self.offset, self.optionsy)
                self.state = 'Controls'
            elif self.state == 'Controls':
                self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
                self.state = 'Levels'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Controls':
                self.game.curr_menu = self.game.options
                self.run_display = False
            elif self.state == "Levels":
                self.game.curr_menu = self.game.levels
                self.run_display = False
                
class ControlsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'Controls'

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            #self.game.display.fill(self.game.BLACK)
            self.game.display.blit(Settings.MENU_BG, (0, 0))
            self.game.draw_text('Game Controls', 40, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2 - 150)
            self.game.draw_text('Menu', 50, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2-85)
            self.game.draw_text('Backspace = Previous Menu', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2-50)
            self.game.draw_text('Enter = Select', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2-25)
            self.game.draw_text('Up Arrow = Move Up', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2)
            self.game.draw_text('Down Arrow = Move Down', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+25)
            self.game.draw_text('Game', 50, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+50)
            self.game.draw_text('Right Arrow = Move Right', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+85)
            self.game.draw_text('Left Arrow = Move Left', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+110)
            self.game.draw_text('Space Bar = Jump', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+135)
            self.game.draw_text('Backspace = Main Menu', 25, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+160)



            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False

class LevelSelection(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Level1"
        self.level1x, self.level1y = self.mid_w, self.mid_h - 40
        self.start = False
        self.level2x, self.level2y = self.mid_w, self.mid_h
        self.level3x, self.level3y = self.mid_w, self.mid_h + 40
        self.level4x, self.level4y = self.mid_w, self.mid_h + 80
        self.level5x, self.level5y = self.mid_w, self.mid_h + 120
        self.level6x, self.level6y = self.mid_w, self.mid_h + 160
        self.cursor_rect.midtop = (self.level1x + self.offset, self.level1y)

    def check_input(self):
        self.move_cursor()
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == "Level1":
                self.game.playing = True
            elif self.state == "Level2":
                self.game.playing = True
            elif self.state == "Level3":
                self.game.playing = True
            elif self.state == "Level4":
                self.game.playing = True
            elif self.state == "Level5":
                self.game.playing = True
            elif self.state == "Level6":
                self.game.playing = True

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            #self.game.display.fill(self.game.BLACK)
            self.game.display.blit(Settings.MENU_BG, (0, 0))

            self.game.draw_text('Level Selection', 75, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/3)

            self.game.draw_text('Level 1', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2-40)
            self.game.draw_text('Level 2', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2)
            self.game.draw_text('Level 3', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+40)
            self.game.draw_text('Level 4', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+80)
            self.game.draw_text('Level 5', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+120)
            self.game.draw_text('Level 6', 40, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+160)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Level1':
                self.cursor_rect.midtop = (self.level2x + self.offset, self.level2y)
                self.state = 'Level2'
            elif self.state == 'Level2':
                self.cursor_rect.midtop = (self.level3x + self.offset, self.level3y)
                self.state = 'Level3'
            elif self.state == 'Level3':
                self.cursor_rect.midtop = (self.level4x + self.offset, self.level4y)
                self.state = 'Level4'
            elif self.state == 'Level4':
                self.cursor_rect.midtop = (self.level5x + self.offset, self.level5y)
                self.state = 'Level5'
            elif self.state == 'Level5':
                self.cursor_rect.midtop = (self.level6x + self.offset, self.level6y)
                self.state = 'Level6'
            elif self.state == 'Level6':
                self.cursor_rect.midtop = (self.level1x + self.offset, self.level1y)
                self.state = 'Level1'

        elif self.game.UP_KEY:
            if self.state == 'Level1':
                self.cursor_rect.midtop = (self.level6x + self.offset, self.level6y)
                self.state = 'Level6'
            elif self.state == 'Level2':
                self.cursor_rect.midtop = (self.level1x + self.offset, self.level1y)
                self.state = 'Level1'
            elif self.state == 'Level3':
                self.cursor_rect.midtop = (self.level2x + self.offset, self.level2y)
                self.state = 'Level2'
            elif self.state == 'Level4':
                self.cursor_rect.midtop = (self.level3x + self.offset, self.level3y)
                self.state = 'Level3'
            elif self.state == 'Level5':
                self.cursor_rect.midtop = (self.level4x + self.offset, self.level4y)
                self.state = 'Level4'
            elif self.state == 'Level6':
                self.cursor_rect.midtop = (self.level5x + self.offset, self.level5y)
                self.state = 'Level5'

        elif self.game.START_KEY:
            if self.state == 'Level1':
                self.run_display = False
                self.start = True
            elif self.state =='Level2':
                self.run_display = False
                self.start = True
            elif self.state == 'Level3':
                self.run_display = False
                self.start = True
            elif self.state == 'Level4':
                self.run_display = False
                self.start = True
            elif self.state == 'Level5':
                self.run_display = False
                self.start = True
            elif self.state == 'Level6':
                self.run_display = False
                self.start = True



