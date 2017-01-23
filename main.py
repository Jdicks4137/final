# josh dickey 1/23/17
# this program creates a game that requires the user to pick up a key, use the key to unlock a door, then walk through
# another door to beat the game

import pygame
import sys
import character
import door1
import door2
import key
from pygame.locals import *


APPLICATION_WIDTH = 600
APPLICATION_HEIGHT = 400

pygame.init()  # this initializes pygame which is important for the text and delay to function properly

main_surface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
pygame.display.set_caption("doom")

main_surface.fill((255, 0, 0))  # this fills the background red

first_door = door1.Enter()  # the two lines below determine the location of the first door on the screen
first_door.rect.x = APPLICATION_WIDTH / 1.4
first_door.rect.y = APPLICATION_HEIGHT / 3

second_door = door2.Freedom()  # the two lines below determine the location of the second door on the screen
second_door.rect.x = APPLICATION_WIDTH / 20
second_door.rect.y = APPLICATION_HEIGHT / 3.5

my_key = key.Unlock()  #  the two lines below determine the location of the key on the screen
my_key.rect.x = APPLICATION_WIDTH / 5
my_key.rect.y = APPLICATION_HEIGHT / 2

my_character = character.Player(8, 8, main_surface)  # the two lines below determine the location of the player on the
# screen
my_character.rect.x = APPLICATION_WIDTH / 2
my_character.rect.y = APPLICATION_HEIGHT / 2

door_group = pygame.sprite.Group()  # this allows contact to be made between the first door and another sprite
door_group.add(first_door)

objective = pygame.sprite.Group()  # this allows contact to be made between the second door and another sprite
objective.add(second_door)

my_key_group = pygame.sprite.Group()  # this allows contact to be made between the key and another sprite
my_key_group.add(my_key)

show_key = True  # this displays the key
has_key = False  # this determines if the user has the key

level_1 = True  # this is floor 1
level_2 = False  # this is floor 2

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if pygame.key.get_pressed()[K_LEFT]:  # this moves the character left if the left arrow key is pressed
        my_character.move_left()

    if pygame.key.get_pressed()[K_RIGHT]:  # this moves the character right if the right arrow key is pressed
        my_character.move_right()

    if pygame.sprite.spritecollide(my_character, my_key_group, True):
        show_key = False  # this removes the key from the screen if the player touches the key
        has_key = True  # this informs the program that the user has the key

    if level_1:  # this displays the first door and the character on the first floor
        main_surface.fill((255, 0, 0))
        main_surface.blit(first_door.image, first_door.rect)
        main_surface.blit(my_character.character, my_character.rect)

    if level_2:  # this displays the second door and the character on the first floor
        main_surface.fill((0, 255, 0))  # green
        main_surface.blit(second_door.image_2, second_door.rect)
        main_surface.blit(my_character.character, my_character.rect)

    if show_key:  # this displays the key on the screen
        main_surface.blit(my_key.image, my_key.rect)

    if pygame.sprite.spritecollide(my_character, door_group, False):
        if has_key:  # this only allows the player to enter the next level if they have the key
            level_1 = False
            level_2 = True

    if pygame.sprite.spritecollide(my_character, objective, False):  # objective refers to second door
        if level_2:  # this ensures that contact between the player and the second door can only be made on level 2
            main_surface.fill((255, 255, 255))  # white
            font_1 = pygame.font.SysFont("Ariel", 30)  # these three lines of code display a message on the screen
            label_1 = font_1.render("You Win!", 1, (0, 0, 0))
            main_surface.blit(label_1, (APPLICATION_WIDTH / 2.25, APPLICATION_HEIGHT / 2.1))
            pygame.display.update()
            pygame.time.wait(2000)  # this ensures the message waits two seconds before leaving the screen
            pygame.quit()
            sys.exit()

    pygame.display.update()
