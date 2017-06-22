import sys
import pygame

from settings import Settings
from dolphin import Dolphin
from fishers import Fisher
import functions
from pygame.sprite import Group

def run_game ():
    #inicjalizacja gry i utworzenie obiektu ekranu
    pygame.init()
    dolphingame_settings=Settings()
    screen=pygame.display.set_mode((dolphingame_settings.screen_width, dolphingame_settings.screen_height))
    pygame.display.set_caption("Dolphin Game")
    #Utworzenie statku kosmicznego
    dolphin=Dolphin(dolphingame_settings,screen)
    bubbles = Group()
    fisher=Fisher(dolphingame_settings,screen)

    #rozpocięcie pętli glownej gry
    while True:

        functions.check_events(dolphingame_settings,screen,dolphin,bubbles)
        dolphin.update()

        functions.update_bubbles(bubbles)
        functions.update_screen(dolphingame_settings, screen, dolphin, fisher, bubbles)
run_game()


