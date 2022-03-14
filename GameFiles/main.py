"""
The file main.py holds the main method for the Freddy Takes on College Game. 
"""

#from game import Game

import pygame
import Settings
import Level_Data
from Level import Level
from Player import Player

mAdventurerPath = ""
BG_IMAGE = pygame.image.load('GameFiles/Assets/GreenHillsBG.png')
BG_IMAGE = pygame.transform.scale(BG_IMAGE, (Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

tile_size = 50

#g = Game()

#while g.running:
    #g.curr_menu.display_menu()
    #g.game_loop()

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

#WIN = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
#pygame.display.set_caption("Freddy Takes on College!")


# grid function used only for level making
def draw_grid():
    for line in range(0, (int(Settings.WINDOW_HEIGHT/tile_size))):
        pygame.draw.line(WIN, (255, 255, 255), (0, line * tile_size), (Settings.WINDOW_WIDTH, line * tile_size))
    for line in range(0, (int(Settings.WINDOW_WIDTH/tile_size))):
        pygame.draw.line(WIN, (255, 255, 255), (line * tile_size, 0), (line * tile_size, Settings.WINDOW_HEIGHT))

level_1 = Level(Level_Data.level1, tile_size, WIN)

def main():
    # GUI/Game code to go here
    clock = pygame.time.Clock()
    run = True
    
    player = Player(100, Settings.WINDOW_HEIGHT-130, 5, 'GameFiles/Assets/character_maleAdventurer_idle.png', 'maleAdventurer')

    #while run:
        #clock.tick(Settings.FPS)

        WIN.blit(BG_IMAGE, (0, 0))
        #draw_grid()
        level_1.draw_level()
        player.update(WIN, level_1) # hard-coded for now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                

        pygame.display.update()

    pygame.quit()

# Make sure main() only runs from this file directly
#if __name__ == "__main__":
    #main()