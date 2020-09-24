from configuration import *
from back_end import Map, Character
import pygame
import sys
pygame.init()


def get_sprite_images(sprite_content):
    # Assigniation d'image pour chaque lettre donnée
    sprite_image = None

    if sprite_content == letter_of_character:
        sprite_image = image_of_character
    if sprite_content == letter_for_walls:
        sprite_image = image_for_walls
    if sprite_content == letter_for_space:
        sprite_image = image_for_space
    if sprite_content == letter_for_ending:
        sprite_image = image_for_ending
    if sprite_content == letter_of_guard:
        sprite_image = image_for_guard
    if sprite_content == number_for_syringe:
        sprite_image = image_syringe
    if sprite_content == number_for_tube:
        sprite_image = image_tube
    if sprite_content == number_for_ether:
        sprite_image = image_ether
    return sprite_image


def draw_map(surface, maze):
    # Injection des images en fonction de la composition du paramètre "maze".
    for j, sprite in enumerate(maze):
        for i, sprite_content in enumerate(sprite):
            #print("{}, {}: {}". format(j, i, sprite_content, sprite))
            my_rect = pygame.Rect(i*sprite_width, j*sprite_eight, 480, 645)
            surface.blit(get_sprite_images(sprite_content), my_rect)


def initialize_game():
    surface = pygame.display.set_mode(display_size)
    pygame.display.set_caption("Mac Gyver Game")
    return surface

# Instancier la classe Character pour donner vie à un joueur
player = Character()
# Instancier la classe Map pour créer une carte
myMap = Map(player)


def game_loop(surface, maze):

    end = myMap.end_position
    x = end[0]
    y = end[1]
    # Ajout de display_functions
    draw_map(surface, maze)
    #pygame.display.update()

    running = True

    while running:
        while myMap.maze[x][y] != letter_of_character:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                    if event.key == pygame.K_RIGHT:
                        myMap.set_movement(input_right)
                    if event.key == pygame.K_LEFT:
                        myMap.set_movement(input_left)
                    if event.key == pygame.K_DOWN:
                        myMap.set_movement(input_down)
                    if event.key == pygame.K_UP:
                        myMap.set_movement(input_up)

            if myMap.end is True:
                # Création du message de fin de jeu
                font = pygame.font.SysFont("Times New Roman, Arial", 20)
                # Render : draw a text on a surface -> render(text, antialias, color, background=None)
                text_lose = font.render("You Lose !", True, RED)
                text_lose_1 = font.render("You must collect all items to beat guard !", True, LIGHTGREY)
                surface.blit(text_lose, (display_width / 2 - text_lose.get_rect().width / 2, display_height / 2))
                surface.blit(text_lose_1, (display_width / 2 - text_lose_1.get_rect().width / 2, display_height / 1.8))
                # draw_map(surface, maze)
                pygame.display.update()
                break
            draw_map(surface, maze)
            pygame.display.update()

        else:
            # Création du message de fin de jeu
            font = pygame.font.SysFont("Times New Roman, Arial", 40)
            # Render : draw a text on a surface -> render(text, antialias, color, background=None)
            text_win = font.render("You WIN !", True, BLUE)
            surface.blit(text_win, (display_width/2 - text_win.get_rect().width/2, display_height/2))
            #draw_map(surface, maze)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    else:
        print("X")