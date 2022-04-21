"""
The file main.py holds the main method for the Freddy Takes on College Game. 
"""

import pygame
from game import Game
import Settings
import Level_Data
from Level import Level
from Player import Player

def main():

    g = Game()

    while g.running:
        g.curr_menu.display_menu()
        if g.levels.start:
            g.game_loop()
    
# Make sure main() only runs from this file directly
if __name__ == "__main__":
    main()