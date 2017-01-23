# josh dickey 1/23/17
# this program creates a class for the character seen in the main file

import pygame


class Player(pygame.sprite.Sprite):
    """this creates a small dot as our character which we will control"""
    def __init__(self, person_width, person_height, screen):
        super().__init__()
        self.screen = screen
        self.person_width = person_width
        self.person_height = person_height
        self.character = pygame.Surface((person_width, person_height))
        self.rect = self.character.get_rect()
        self.speed = 3
 
    def move_left(self):
        """this allows the character to move left between the given parameters"""
        if self.rect.x > 0:
            self.rect.x -= self.speed

    def move_right(self):
        """this allows the character to move right between the given parameters"""
        if self.rect.x < self.screen.get_width() - (self.person_width + self.speed):
            self.rect.x += self.speed
