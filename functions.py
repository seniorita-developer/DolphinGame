import sys
from time import sleep
import pygame
from bubble import Bubble
from fishers import Fisher

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


def check_events(dolphingame_settings,screen, stats, dolphin_scores,play_button, dolphin,fishers,bubbles):
    '''Reakcja na zdarzenia generowane przez klawiaturę i mysz'''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            check_keydown_events(event, dolphingame_settings,screen,dolphin,bubbles)


        elif event.type==pygame.KEYUP:
            check_keyup_events(event,dolphin)

        elif event.type==pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y=pygame.mouse.get_pos()

            check_play_button(dolphingame_settings,screen,stats,dolphin_scores,play_button,dolphin,fishers,bubbles,mouse_x,mouse_y)

def check_play_button(dolphingame_settings,screen,stats,dolphin_scores, play_button,dolphin,fishers,bubbles,mouse_x,mouse_y):
    button_clicked=play_button.rect.collidepoint(mouse_x,mouse_y)
    if button_clicked and not stats.game_active:
        #Wyzerowanie ustaiwen gry
        dolphingame_settings.initialize_dynamic_settings()

        pygame.mouse.set_visible(False)

        stats.reset_stats()
        stats.game_active=True

        dolphin_scores.prepare_score()
        dolphin_scores.prepare_high_score()
        dolphin_scores.prepare_level()

        #Usunięcie zawarości list fishers i bubbles
        fishers.empty()
        bubbles.empty()

        #Utworzenie nowych rybaków i wyśrodkowanie delfina
        create_fishers(dolphingame_settings,screen,dolphin,fishers)
        dolphin.center_dolphin()

def update_screen(dolphingame_settings,screen,stats, dolphin_scores, dolphin,fishers, bubbles,play_button):
    '''Uaktualnienie obrazów na ekranie i przejście do nowego ekranu'''
    # odswieżenie ekranu w trakcie każdej iteracji pętli
    screen.fill(dolphingame_settings.bg_color)
    for bubble in bubbles.sprites():
        bubble.draw_bubble()

    dolphin.blitme()
    fishers.draw(screen)
    #Wyświetlenie informacji o punktacji
    dolphin_scores.show_score()

    #Wyświetlenie przycisku kiedy gra jest nieaktywna
    if not stats.game_active:
        play_button.draw_button()
    # wyświetlanie ostatnio zmodyfikowanego ekranu.
    pygame.display.flip()

def check_bubble_ship_collisions(dolphingame_settings,screen,stats,dolphin_scores,dolphin,fishers, bubbles):
    collisions = pygame.sprite.groupcollide(bubbles, fishers, False, True)
    if collisions:
        for fishers in collisions.values():
            stats.score+=dolphingame_settings.dolphin_points*len(fishers)
            dolphin_scores.prepare_score()
        check_high_score(stats,dolphin_scores)

    if len(fishers)==0:
        #Usunięcie istniejących pocisków, przyspieszenie gry i utworzenie nowej floty
        bubbles.empty()
        dolphingame_settings.increase_speed()

        stats.level+=1
        dolphin_scores.prepare_level()

        create_fishers(dolphingame_settings,screen,dolphin,fishers)


def update_bubbles(dolphingame_settings,screen,stats, dolphin_scores, dolphin,fishers, bubbles):
    '''Uaktualnienie polożenia pocisków i usunięcie tych niewidocznych na ekranie'''
    bubbles.update()

    for bubble in bubbles.copy():
        if bubble.rect.left <= 0:
            bubbles.remove(bubble)
    #Sprawdzenie czy bąbelki trafili w statek
    check_bubble_ship_collisions(dolphingame_settings,screen,stats,dolphin_scores, dolphin,fishers, bubbles)



def get_number_fishers_y (dolphingame_settings,fisher_height):
    available_space_y = dolphingame_settings.screen_height - (2 * fisher_height)
    number_fishers_y = int(available_space_y / (2 * fisher_height))
    return number_fishers_y


def get_number_lines(dolphingame_settings,dolphin_width,fisher_width):
    '''Ustalenie ile linii zmieszci się na ekranie'''
    available_space_x = (dolphingame_settings.screen_width - (3* fisher_width)-dolphin_width)
    number_lines = int((available_space_x / (2 * fisher_width))/2)
    return number_lines


def create_fisher(dolphingame_settings,screen,fishers,fisher_number,line_number):
    '''Utworzenie statku i umieszczenie go w linii'''
    fisher = Fisher(dolphingame_settings, screen)
    fisher_height=fisher.rect.height
    fisher.y = fisher_height + 2 * fisher_height * fisher_number
    fisher.rect.y = fisher.y
    fisher.rect.x=fisher.rect.width + 2*fisher.rect.width * line_number
    fishers.add(fisher)

def create_fishers(dolphingame_settings,screen,dolphin,fishers):
    """Utworzenie wielu statków rybackich"""
    #Utworzenie statku rybackiego i ustalenie liczby statków w linii
    #Odleglość pomiędzy poszczególnymy statkami równa wysokości statku
    fisher = Fisher(dolphingame_settings, screen)
    number_fishers_y=get_number_fishers_y(dolphingame_settings,fisher.rect.height)
    number_lines=get_number_lines(dolphingame_settings,dolphin.rect.width,fisher.rect.width)

    #Utworzenie kilku linii statków
    for line_number in range(number_lines):
        for fisher_number in range (number_fishers_y):
            create_fisher(dolphingame_settings,screen,fishers,fisher_number,line_number)


def check_fishers_edges(dolphingame_settings,fishers):
    '''Odpowiednia reakcja kiedy statek dotrze do krawędzi ekranu'''
    for fisher in fishers.sprites():
        if fisher.check_edges():
            change_fishers_direction(dolphingame_settings,fishers)
            break

def change_fishers_direction(dolphingame_settings,fishers):
    '''Przesunięcie wzystkich statków w prawo i zmiana kierunku w którym one sie poruszają'''
    for fisher in fishers.sprites():
        fisher.rect.x+= dolphingame_settings.fishers_drop_speed
    dolphingame_settings.fishers_direction *= -1

def dolphin_hit(dolphingame_settings,stats,screen,dolphin,fishers,bubbles):
    '''Reakcja na uderzenie statku w delphina'''
    if stats.dolphins_left > 0:
        #Zmniejszenie wartości przechowywanej w dolphins_left
        stats.dolphins_left -=1

        #Usunięcie zawartości list fishers i bbubbles
        fishers.empty()
        bubbles.empty()

        #Utworzenie nowych statków i wyśrodkowanie delfina
        create_fishers(dolphingame_settings,screen,dolphin,fishers)
        dolphin.center_dolphin()

        #Pauza
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)

def update_fishers(dolphingame_settings,stats,screen,dolphin,fishers,bubbles):
    '''Sprawdzenie czy statki znajdują się przy krawędzi
    ekranu a następnie uaktualnienie położenia wszystkich statków na ekranie'''
    check_fishers_edges(dolphingame_settings, fishers)
    fishers.update()
    # Wykrywanie kolizji pomiędzy statkiem a delfinem
    if pygame.sprite.spritecollideany(dolphin, fishers):
        dolphin_hit(dolphingame_settings, stats, screen, dolphin, fishers, bubbles)

def check_high_score(stats,dolphin_scores):
    '''Sprawdzenie czy mamy nowy najlepszy wynik osiągnięty dotąd w grze'''
    if stats.score>stats.high_score:
        stats.high_score=stats.score
        dolphin_scores.prepare_high_score()
