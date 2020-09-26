from configuration import *
from back_end import Character
from random import randint
import pygame
pygame.init()


class Map:

    def __init__(self, player):
        self.maze = []
        self.character = player
        self.read_maze_txt()
        self.find_player_position()
        self.set_objects()
        self.display_map()
        self.objects = self.character.objects
        self.end_position = (0, 0)
        self.find_end_position()
        self.finish = "playing"

    def read_maze_txt(self):
        two_dimensions_list = []
        with open(config_file, "r") as file:
            txt_reading = file.read().splitlines()
            for line in txt_reading:
                list_letter = [i for i in line]
                two_dimensions_list.append(list_letter)
            self.maze = two_dimensions_list

    # Better display in terminal
    def display_map(self):
        for x in range(max_x):
            print(self.maze[x])

    def find_player_position(self):
        for x in range(max_x):
            for y in range(max_y):
                if self.maze[x][y] is letter_of_character:
                    self.character.set_coordinates(x, y)

    def find_end_position(self):
        for x in range(max_x):
            for y in range(max_y):
                if self.maze[x][y] is letter_for_ending:
                    self.end_position = (x, y)

    # Set objects randomly
    def set_objects(self):
        list_of_positions = []
        number_of_objects = 1

        for x in range(max_x):
            for y in range(max_y):
                if self.maze[x][y] is letter_for_space:
                    free_position = (x, y)
                    list_of_positions.append(free_position)
        total_free_spaces = len(list_of_positions) - 1
        if total_free_spaces >= max_objects - 1:
            for i in range(max_objects):
                # Use of random function
                random_int = randint(0, total_free_spaces)
                object_coordinates = list_of_positions[random_int]
                list_of_positions.remove(object_coordinates)
                total_free_spaces -= 1
                x = object_coordinates[0]
                y = object_coordinates[1]
                self.maze[x][y] = number_of_objects
                number_of_objects += 1

    def set_movement(self, input_type):
        x = self.character.x
        y = self.character.y

        input_move = {
            input_up: {
                "x": -1,
                "y": 0
            },
            input_down: {
                "x": +1,
                "y": 0
            },
            input_left: {
                "x": 0,
                "y": -1
            },
            input_right: {
                "x": 0,
                "y": +1
            },

        }
        if input_type in input_move:
            self.do_movement(x + input_move[input_type]["x"], y + input_move[input_type]["y"])
        else:
            print("Something wrong in set_movement function")

    def do_movement(self, new_x, new_y):

        if new_x in range(max_x) and new_y in range(max_y):
            target_position = str(self.maze[new_x][new_y])
            if target_position != letter_for_walls:
                if target_position == letter_for_space:
                    self.update_map(new_x, new_y)
                if target_position.isnumeric():
                    self.update_map(new_x, new_y)
                    self.objects = self.objects + 1
                if target_position == letter_of_guard:
                    if self.objects == max_objects:
                        self.update_map(new_x, new_y)
                        print("Guard is now sleeping !")
                    if self.objects != max_objects:
                        self.finish = "lose"
                        print("You lose :( ")
                if target_position == letter_for_ending:
                    self.update_map(new_x, new_y)
                    self.finish = "win"
                    print("You Win !")
            else:
                print("There is a wall you can't go that way ! ")
        else:
            print("Player can't go out of the maze")

    def update_map(self, new_x, new_y):
        x = self.character.x
        y = self.character.y

        self.maze[x][y] = letter_for_space
        self.character.move(new_x, new_y)
        self.maze[new_x][new_y] = letter_of_character
        self.find_player_position()
        self.display_map()