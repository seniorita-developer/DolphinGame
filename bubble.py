import pygame
from pygame.sprite import Sprite


class Bubble(Sprite):
    '''Klasa przeznaczona do zarządzania bąbelkami wystrzeliwanymi przez delfina'''
    def __init__(self, dolphingame_settings, screen, dolphin):

        '''Utworzenie obiektu pocisku w aktualnym położeniu delfina'''
        super(Bubble, self).__init__()
        self.screen = screen
        image = pygame.image.load('images/bubble.bmp')
        self.image = pygame.transform.scale(image, (15, 15))
        self.rect = pygame.Rect(0, 0, dolphingame_settings.bubble_width, dolphingame_settings.bubble_height)

        self.rect.center = dolphin.rect.center
        self.rect.top = dolphin.rect.centery

        #polożenie pocisku jest zdefinowane za pomocą wartości zmiennoprzecinkowej
        self.x = float(self.rect.x)
        self.speed_factor = dolphingame_settings.bubble_speed_factor

    def update(self):
        '''Poruszanie pociskiem po ekranie'''
        self.x-= self.speed_factor
        self.rect.x = self.x

    def draw_bubble(self):
        '''Wyświetlenie pocisku na ekranie'''
        self.screen.blit(self.image, self.rect)
