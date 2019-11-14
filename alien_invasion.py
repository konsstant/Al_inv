import sys
import pygame
import sqlite3
from pygame.locals import *
from setting import Settings
from ship import Ship
import game_functions as gf
import bullet
from pygame.sprite import Group
import Alien
from Alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard



def run_game():

    pygame.init()
    ai_settings=Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    play_button=Button(ai_settings,screen,"Play")

    ship=Ship(ai_settings,screen)

    bullets=Group()

    aliens=Group()

    gf.create_fleet(ai_settings,screen,ship,aliens)

    stats=GameStats(ai_settings)

    sb=Scoreboard(ai_settings,screen,stats)

    bg_fill=(230,230,230)
    Gameexit=True

    alient=Alien(ai_settings,screen)

    while Gameexit:

        gf.check_events(ai_settings,screen,ship,bullets,stats,play_button,aliens,sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings,screen,ship,bullets,aliens,sb,stats)
            gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets,sb)
        gf.update_screen(ai_settings,screen,ship,aliens,bullets,play_button,stats,sb)


run_game()