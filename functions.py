import sys
import pygame
from bubble import Bubble

def check_keydown_events(event, dolphingame_settings, screen, dolphin,bubbles):
    #reakcja na naciśnięcie klawisza
    if event.key == pygame.K_RIGHT:
        dolphin.moving_right = True
    elif event.key == pygame.K_LEFT:
        dolphin.moving_left = True
    elif event.key == pygame.K_UP:
        dolphin.moving_up = True
    elif event.key == pygame.K_DOWN:
        dolphin.moving_down = True

    elif event.key == pygame.K_SPACE:
        #Utworzenie nowego pocisku i dodanie go do grupy pocisków
        fire_bubble(dolphingame_settings,screen,dolphin,bubbles)


def fire_bubble(dolphingame_settings,screen,dolphin,bubbles):
    '''Wystrzelenie pocisku jeśli nie przekroczono limit'''
    if len(bubbles) < dolphingame_settings.bubble_allowed:
        new_bubble = Bubble(dolphingame_settings, screen, dolphin)
        bubbles.add(new_bubble)

def check_keyup_events(event,dolphin):
    #reakcja na zwolnienie klawisza
    if event.key == pygame.K_RIGHT:
        dolphin.moving_right = False
    elif event.key == pygame.K_LEFT:
        dolphin.moving_left = False
    elif event.key == pygame.K_UP:
        dolphin.moving_up = False
    elif event.key == pygame.K_DOWN:
        dolphin.moving_down = False


def check_events(dolphingame_settings,screen, dolphin,bubbles):
    '''Reakcja na zdarzenia generowane przez klawiaturę i mysz'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, dolphingame_settings,screen,dolphin,bubbles)


        elif event.type==pygame.KEYUP:
            check_keyup_events(event,dolphin)

def update_screen(dolphingame_settings,screen,dolphin,fisher, bubbles):
    '''Uaktualnienie obrazów na ekranie i przejście do nowego ekranu'''
    # odswieżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(dolphingame_settings.bg_color)
    for bubble in bubbles.sprites():
        bubble.draw_bubble()


    dolphin.blitme()
    fisher.blitme()

    # wyświetlanie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()

def update_bubbles(bubbles):
    '''Uaktualnienie polożenia pocisków i usunięcie tych niewidocznych na ekranie'''
    bubbles.update()

    for bubble in bubbles.copy():
        if bubble.rect.left <= 0:
            bubbles.remove(bubble)