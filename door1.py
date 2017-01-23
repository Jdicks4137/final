# josh dickey 1/23/17
# this program creates a class for the first door seen in the main file

import pygame


class Enter(pygame.sprite.Sprite):
    """this creates a sprite that looks like a door"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("BcarBkaKi.jpg").convert()
        self.rect = self.image.get_rect()