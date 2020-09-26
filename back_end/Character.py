from configuration import *
import pygame
pygame.init()


class Character(pygame.sprite.Sprite):
    objects = 0

    def __init__(self):
        # super() Initialize Sprite class
        super().__init__()
        self.image = image_of_character
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def set_coordinates(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y