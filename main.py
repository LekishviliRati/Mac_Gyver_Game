from front_end import display_functions
import pygame
pygame.init()


def main():

    # Initialize surface
    surface = display_functions.initialize_game()
    # Start game
    display_functions.game_loop(surface, display_functions.myMap.maze)


if __name__ == "__main__":
    main()



