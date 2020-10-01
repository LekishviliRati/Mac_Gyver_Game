import pygame
pygame.init()


# Config file where to find the map
config_file = "maze_structure.txt"

# Variables for elements in Map
letter_for_walls = "W"
letter_of_character = "S"
letter_of_guard = "G"
letter_for_space = "R"
letter_for_ending = "E"
number_for_syringe = 1
number_for_tube = 2
number_for_ether = 3


# Input for user to Use
input_up = "z"
input_down = "s"
input_left = "q"
input_right = "d"


# Dimensions for the map
min_y = 0
max_y = 15
min_x = 0
max_x = 15

# Count of maximum objects in map
max_objects = 3

# Images
image_of_character = pygame.image.load("assets/MacGyver_1.png")
image_for_walls = pygame.image.load("assets/wall_1.png")
image_for_space = pygame.image.load("assets/space.png")
image_for_guard = pygame.image.load("assets/Guard.png")
image_syringe = pygame.image.load("assets/syringe.png")
image_tube = pygame.image.load("assets/plastic_tube.png")
image_ether = pygame.image.load("assets/ether_2.png")
image_for_ending = pygame.image.load("assets/exit.png")


# Display
display_size = width, height = 480, 645
display_width = 480
display_height = 645
background_color = 84, 82, 89
sprite_width = 32
sprite_eight = 43


# Colors
GREY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (55, 55, 255)
BLACK = (0, 0, 0)
GREEN = (0, 200, 0)
DARKGREY = (150, 150, 150)
LIGHTGREY = (210, 210, 210)
UGLY_PINK = (255, 0, 255)
BROWN = (153, 76, 0)
GOLD = (153, 153, 0)
DARKGREEN = (0, 102, 0)
DARKORANGE = (255, 128, 0)
