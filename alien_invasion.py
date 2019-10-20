import sys
import pygame
import sqlite3
from pygame.locals import *
from setting import Settings
from ship import Ship
import game_functions as gf


def run_game():

    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship=Ship(screen)

    bg_fill=(230,230,230)
    Gameexit=True

    while Gameexit:

        #screen.fill(ai_settings.bg_color)

        #ship.blitme()

        gf.check_events(ship)

        #for event in pygame.event.get():
        #   if event.type==QUIT:
        #       sys.exit()

        #pygame.display.flip()
        gf.update_screen(ai_settings,screen,ship)


run_game()


#display_test()

#def Kaboom():