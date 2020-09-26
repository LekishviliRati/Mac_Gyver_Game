from configuration import *
from back_end import Map, Character
import pygame
import sys
pygame.init()


class Display:

    def __init__(self):
        self.player = Character()
        self.my_map = Map(self.player)
        self.surface = self.initialize_game()
        self.maze = self.my_map.maze
        self.draw_map(self.surface, self.maze)
        self.game_loop(self.surface, self.maze)

    @classmethod
    def initialize_game(cls):
        # Creates pygame surface
        surface = pygame.display.set_mode(display_size)
        pygame.display.set_caption("Mac Gyver Game")
        return surface

    @classmethod
    def get_sprite_image(cls, sprite_content):

        letter_image_association = {
                letter_of_character: {
                    "image": image_of_character
                },
                letter_for_walls: {
                    "image": image_for_walls
                },
                letter_for_space: {
                    "image": image_for_space
                },
                letter_for_ending: {
                    "image": image_for_ending
                },
                letter_of_guard: {
                    "image": image_for_guard
                },
                number_for_syringe: {
                    "image": image_syringe
                    },
                number_for_tube: {
                    "image": image_tube
                },
                number_for_ether: {
                    "image": image_ether
                },
        }

        if sprite_content in letter_image_association:
            sprite_image = letter_image_association[sprite_content]["image"]
            return sprite_image

    def draw_map(self, surface, maze):
        # Set images for each letter on pygame surface
        for j, sprite in enumerate(maze):
            for i, sprite_content in enumerate(sprite):
                my_rect = pygame.Rect(i*sprite_width, j*sprite_eight, 480, 645)
                surface.blit(self.get_sprite_image(sprite_content), my_rect)

    @classmethod
    def close_function(cls):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def game_loop(self, surface, maze):

        running = True

        move = {
            pygame.K_RIGHT: {
                "direction": input_right
            },
            pygame.K_LEFT: {
                "direction": input_left
            },
            pygame.K_DOWN: {
                "direction": input_down
            },
            pygame.K_UP: {
                "direction": input_up
            },
        }

        while running:
            while self.my_map.finish == "playing":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key in move:
                            direction = move[event.key]["direction"]
                            self.my_map.set_movement(direction)

                self.draw_map(surface, maze)
                pygame.display.update()

            if self.my_map.finish == "lose":
                font = pygame.font.SysFont("Times New Roman, Arial", 20)
                text_lose = font.render("You Lose !", True, RED)
                text_lose_1 = font.render("You must collect all items to beat guard !", True, LIGHTGREY)
                surface.blit(text_lose, (display_width / 2 - text_lose.get_rect().width / 2, display_height / 2))
                surface.blit(text_lose_1, (display_width / 2 - text_lose_1.get_rect().width / 2, display_height / 1.8))
                pygame.display.update()
                self.close_function()

            if self.my_map.finish == "win":
                font = pygame.font.SysFont("Times New Roman, Arial", 40)
                text_win = font.render("You WIN !", True, BLUE)
                surface.blit(text_win, (display_width/2 - text_win.get_rect().width/2, display_height/2))
                pygame.display.update()
                self.close_function()

        else:
            print("X")