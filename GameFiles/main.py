"""
The file main.py holds the main method for the Freddy Takes on College Game. 
"""
from game import Game
import pygame
import Settings

g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()

#WIN = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))
#pygame.display.set_caption("Freddy Takes on College!")

#def main():
    # GUI/Game code to go here
    #clock = pygame.time.Clock()
    #run = True

    #while run:
        #clock.tick(Settings.FPS)

        #for event in pygame.event.get():
            #if event.type == pygame.QUIT:
                #run = False
                
    #pygame.quit()

# Make sure main() only runs from this file directly
#if __name__ == "__main__":
    #main()