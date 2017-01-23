# josh dickey 1/23/17
# this program creates a class for the key seen in the main file

import pygame

class Unlock(pygame.sprite.Sprite):
    """this creates a sprite that displays a picture of a key"""
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("key-clipart-key-clipart-ycoekx9di.png").convert()
        self.rect = self.image.get_rect()