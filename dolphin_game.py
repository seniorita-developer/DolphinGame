import sys
import pygame

from settings import Settings
from game_stats import GameStats
from button import Button
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
    play_button=Button(dolphingame_settings, screen,"Play")
    stats=GameStats(dolphingame_settings)

    #Utworzenie statku rybackiego
    dolphin=Dolphin(dolphingame_settings,screen)
    bubbles = Group()
    fishers=Group()

    #Utworzenie wielu statków
    functions.create_fishers(dolphingame_settings,screen,dolphin,fishers)

    #rozpocięcie pętli glownej gry
    while True:

        functions.check_events(dolphingame_settings,screen,stats, play_button,dolphin,fishers,bubbles)
        if stats.game_active:
            dolphin.update()
            functions.update_fishers(dolphingame_settings, stats,screen, dolphin, fishers, bubbles)
            functions.update_bubbles(dolphingame_settings,screen,dolphin,fishers,bubbles)
        functions.update_screen(dolphingame_settings, screen, stats,dolphin, fishers, bubbles,play_button)
run_game()


