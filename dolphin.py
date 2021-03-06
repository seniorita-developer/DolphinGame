import pygame
from pygame.sprite import Sprite

class Dolphin(Sprite):
    def __init__(self,dolphingame_settings,screen):

        #inicjalizacja delfina i jego położenie początkowe.
        super(Dolphin,self).__init__()
        self.screen=screen
        self.dolphingame_settings=dolphingame_settings

        #wczytanie obrazu statku i pobranie jego prostokąta.
        self.image=pygame.image.load('images/dolphin.bmp')
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #Każdy nowy delfin pojawia się na środku ekranu.
        self.rect.centerx=self.screen_rect.centerx
        self.rect.center =self.screen_rect.center

        self.center=float(self.rect.centerx)

        #opcje wskazujące na poruszanie się delfina
        self.moving_right=False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):

        #Uaktualnienie wartości punktu środkowego delfina, a nie jego prostokąta

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center+=self.dolphingame_settings.dolphin_speed_factor
        if self.moving_left and self.rect.left >0:
            self.center -= self.dolphingame_settings.dolphin_speed_factor

        if self.moving_up and self.rect.top >0:
            self.rect.centery-=self.dolphingame_settings.dolphin_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.centery+= self.dolphingame_settings.dolphin_speed_factor



        #Uaktualnienie obiektu rect na podstawie wartości self.center.
        self.rect.centerx=self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def center_dolphin(self):
        #Umieszczenie delfina na środku ekranu
        self.center=self.screen_rect.centerx
