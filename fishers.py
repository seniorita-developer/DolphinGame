import pygame
from pygame.sprite import Sprite

class Fisher(Sprite):

    def __init__(self,dolphingame_settings,screen):
        #Inicjalizacja statku
        super (Fisher,self).__init__()
        self.screen=screen
        self.dolphingame_settings=dolphingame_settings

        self.image = pygame.image.load('images/fisher.bmp')
        self.rect = self.image.get_rect()

        # Umieszczenie statku w lewym górnym rogu
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Przechowywanie położenia statku
        self.y = float(self.rect.y)

    def blitme(self):
        self.screen.blit(self.image,self.rect)


    def check_edges(self):
        screen_rect=self.screen.get_rect()
        if self.rect.bottom>=screen_rect.bottom:
            return True
        elif self.rect.top <=0:
            return True

    def update(self):
        '''Przesunięcie statku w dól'''
        self.y+=(self.dolphingame_settings.fisher_speed_factor * self.dolphingame_settings.fishers_direction)
        self.rect.y=self.y


