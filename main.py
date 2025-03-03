import pygame as pg
import random
import math
from pygame import mixer

pg.init()

#-------Zmienne--------#
SCR_WG = 1000
SCR_HG = 800
screen = pg.display.set_mode((SCR_WG, SCR_HG))

score_val = 0
scoreX = 5
scoreY = 5
game_over_font = pg.font.Font("freesansbold.ttf", 20)
#----------------------#

#-------Okno-----------#
pg.display.set_caption("Welcome to Space Inviders Game by: GemanoutGames Studio")
#----------------------#

#-----Końcówka nauki------#