import pygame
import random
import math
from pygame import mixer

pygame.init()

screen_width = 1000
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Welcome to Space Inviders Game by: GemiGames Studio")

score_val = 0
scoreX = 5
scoreY = 5
game_over_font = pygame.font.Font("freesansbold.ttf", 20)

dalej mi sie nie chcialo uczyc lol