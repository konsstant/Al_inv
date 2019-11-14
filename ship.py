import pygame
from pygame.sprite import Sprite

class Life (pygame.sprite.Sprite):

    def __init__(self,ai_settings,screen):
        super(Life,self).__init__()
        self.image = pygame.image.load('ship_01.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

class Ship():

    def __init__(self,ai_settings,screen):

        self.screen=screen

        self.ai_settings=ai_settings

        self.image=pygame.image.load('ship_00.png')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        self.rect.centerx=self.screen_rect.centerx
        self.rect.bottom=self.screen_rect.bottom

        self.moving_right=False
        self.moving_left = False

        self.center=float(self.rect.centerx)

    def update(self):
        if self.moving_right and self.rect.right<self.screen_rect.right :
            #self.rect.centerx+=1
            self.center+=self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left>0 :
            #self.rect.centerx-=1
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image,self.rect)

    def center_ship(self):
        self.center=self.screen_rect.centerx