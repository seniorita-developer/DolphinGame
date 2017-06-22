import pygame
from pygame.sprite import Sprite


class Bubble(Sprite):
    '''Klasa przeznaczona do zarządzania pociskami wystrzeliwanymi przez statek'''
    def __init__(self,dolphingame_settings,screen,dolphin):

        '''Utworzenie obiektu pocisku w aktualnym położeniu delfina'''
        super(Bubble,self).__init__()
        self.screen=screen

        self.rect=pygame.Rect(0,0, dolphingame_settings.bubble_width, dolphingame_settings.bubble_height)

        self.rect.center=dolphin.rect.center
        self.rect.top=dolphin.rect.centery

        #polożenie pocisku jest zdefinowane za pomocą wartości zmiennoprzecinkowej
        self.x=float(self.rect.x)


        self.color=dolphingame_settings.bubble_color
        self.speed_factor=dolphingame_settings.bubble_speed_factor


    def update(self):
        '''Poruszanie pociskiem po ekranie'''
        self.x-=self.speed_factor
        self.rect.x=self.x

    def draw_bubble(self):
        '''Wyświetlenie pocisku na ekranie'''
        pygame.draw.rect(self.screen,self.color,self.rect)
