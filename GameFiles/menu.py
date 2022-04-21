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
        self.game.draw_text('[', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Levels"
        self.levelsx, self.levelsy = self.mid_w, self.mid_h + 30
        self.optionsx, self.optionsy = self.mid_w, self.mid_h + 50
        self.cursor_rect.midtop = (self.levelsx + self.offset, self.levelsy)
        pygame.display.set_caption("FTOC")


    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Freddy Takes on College!', 50, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2 - 20)
            self.game.draw_text("Level Selection", 20, self.levelsx, self.levelsy)
            self.game.draw_text("Controls", 20, self.optionsx, self.optionsy)
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
            if self.state == 'Start':
                self.game.playing = True
            elif self.state == 'Controls':
                self.game.curr_menu = self.game.options
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
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Game Controls', 40, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2 - 60)
            self.game.draw_text('Menu', 30, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2-30)
            self.game.draw_text('Backspace = Previous Menu', 12, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2-15)
            self.game.draw_text('Enter = Select', 12, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2)
            self.game.draw_text('Up Arrow = Move Up', 12, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+15)
            self.game.draw_text('Down Arrow = Move Down', 12, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+30)
            self.game.draw_text('Game', 30, Settings.WINDOW_WIDTH / 2, Settings.WINDOW_HEIGHT / 2+45)


            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False


class LevelSelection(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state= "Level1"
        self.level1x, self.level1y = self.mid_w, self.mid_h + 30
        self.start = False
        self.level2x, self.level2y = self.mid_w, self.mid_h + 50
        self.level3x, self.level3y = self.mid_w, self.mid_h + 70
        self.level4x, self.level4y = self.mid_w, self.mid_h + 90
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

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)

            self.game.draw_text('Level Selection', 30, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/3)

            self.game.draw_text('Level 1', 20, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+30)
            self.game.draw_text('Level 2', 20, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+50)
            self.game.draw_text('Level 3', 20, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+70)
            self.game.draw_text('Level 4', 20, Settings.WINDOW_WIDTH/2, Settings.WINDOW_HEIGHT/2+90)
            self.draw_cursor()
            self.blit_screen()
            #this is where you would add our game levels


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
                self.cursor_rect.midtop = (self.level1x + self.offset, self.level1y)
                self.state = 'Level1'
        elif self.game.UP_KEY:
            if self.state == 'Level1':
                self.cursor_rect.midtop = (self.level4x + self.offset, self.level4y)
                self.state = 'Level4'
            elif self.state == 'Level2':
                self.cursor_rect.midtop = (self.level3x + self.offset, self.level3y)
                self.state = 'Level3'
            elif self.state == 'Level3':
                self.cursor_rect.midtop = (self.level2x + self.offset, self.level2y)
                self.state = 'Level4'
            elif self.state == 'Level4':
                self.cursor_rect.midtop = (self.level1x + self.offset, self.level1y)
                self.state = 'Level1'
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



