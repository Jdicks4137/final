# josh dickey 1/23/17
# this program creates a class for the second door seen in the main file

import pygame


class Freedom(pygame.sprite.Sprite):
    """this creates a sprite that looks like a different door"""
    def __init__(self):
        super().__init__()
        self.image_2 = pygame.image.load("door-575959__340.png").convert()
        self.rect = self.image_2.get_rect()
