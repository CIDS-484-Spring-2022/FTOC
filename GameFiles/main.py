"""
The file main.py holds the main method for the 'Lost in the Mountains' Game. 
"""

from game import Game
import Settings

def main():

    g = Game()

    while g.running:
        Settings.GAME_OVER=0
        g.curr_menu.display_menu()
        if g.levels.start:
            g.curr_menu.run_display = False
            g.game_loop()

# Make sure main() only runs from this file directly
if __name__ == "__main__":
    main()