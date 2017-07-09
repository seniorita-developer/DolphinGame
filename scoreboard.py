import pygame.font
from pygame.sprite import Group

from dolphin import Dolphin
class Scoreboard():
    '''Klasa przeznaczona dla przedstawiania informacji o punktacji'''

    def __init__(self,dolpingame_settings,screen,stats):

        self.screen=screen
        self.screen_rect=screen.get_rect()
        self.dolphingame_settings=dolpingame_settings
        self.stats=stats

        self.text_color=(60,30,30)
        self.font=pygame.font.SysFont(None,44)
        self.prepare_score()
        self.prepare_high_score()
        self.prepare_level()
        self.prepare_dolphins()


    def prepare_score(self):
        '''Przekształcenie punktacji na wygenerowany obraz'''
        rounded_score = int(round(self.stats.score,-1))
        score_str="{:,}".format(rounded_score)
        self.score_image=self.font.render(score_str,True,self.text_color,self.dolphingame_settings.bg_color)

        #Wyświetlanie punktacji w prawym górnym rogu ekranu pod najlepszym wynikiem
        self.score_rect=self.score_image.get_rect()
        self.score_rect.right=self.screen_rect.right-20
        self.score_rect.top=50

    def prepare_high_score(self):
        '''Konwersja najlepszego wyniku w prze na wygenerowany obraz'''
        high_score= int(round(self.stats.high_score,-1))
        high_score_str="{:,}".format(high_score)
        self.high_score_image=self.font.render(high_score_str,True,self.text_color,self.dolphingame_settings.bg_color)

        #Wyświetlanie najlepszego wyniku w prawym górnym rogu ekranu
        self.high_score_rect=self.high_score_image.get_rect()
        self.high_score_rect.right=self.screen_rect.right-20
        self.high_score_rect.top=20

    def show_score(self):
        #Wyświetlenie punktacji na ekranie

        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.dolphins.draw(self.screen)

    def prepare_level(self):
        '''Konwertacja numeru poziomu na wygenerowany obraz'''
        self.level_image = self.font.render(str(self.stats.level), True, self.text_color, self.dolphingame_settings.bg_color)

        # Wyświetlanie punktacji w prawym górnym rogu ekranu pod punktacją
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right - 20
        self.level_rect.top = self.score_rect.bottom+20

    def prepare_dolphins(self):
        '''Wyświetla liczbę delfinow, ktore pozostaly graczowi'''
        self.dolphins=Group()
        for dolphin_number in range(self.stats.dolphins_left):
            dolphin=Dolphin(self.dolphingame_settings,self.screen)
            dolphin.rect.right=self.level_rect.right - dolphin_number*dolphin.rect.width
            dolphin.rect.y= self.screen_rect.bottom-dolphin.rect.height-20
            self.dolphins.add(dolphin)


