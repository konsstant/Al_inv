import sys
import pygame
from pygame.locals import *

def check_events(ship):
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
             if event.key==pygame.K_RIGHT:
                #self.rect.centerx = self.screen_rect.centerx
                ship.rect.centerx+=1
                pass

def update_screen (ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    pygame.display.flip()