# -*- coding: utf-8 -*-

"""Character class instantiates a player as a sprite and set coordinates."""

from configuration import image_of_character
import pygame
pygame.init()


class Character(pygame.sprite.Sprite):
    """Instantiate a player as a sprite."""

    objects = 0

    def __init__(self):
        """Initialise Character class."""
        # super() Initialize Sprite class
        super().__init__()
        self.image = image_of_character
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0

    def set_coordinates(self, new_x, new_y):
        """Initialise coordinates."""
        self.x = new_x
        self.y = new_y

    def move(self, new_x, new_y):
        """Update coordinates."""
        self.x = new_x
        self.y = new_y
