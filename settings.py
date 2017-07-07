class Settings():
    '''Klasa do przechowywania wszystkich ustawień gry'''

    def __init__(self):
        #Inicjalizacja danych statystycznych gry

        self.screen_width=1200
        self.screen_height=650
        self.bg_color=(0,100,255)


        self.dolphin_limit=4

        self.bubble_width = 6
        self.bubble_height = 6
        self.bubble_color = 255, 0, 0
        self.bubble_allowed = 5


        self.fishers_drop_speed=10



        #Łatwa zmiana szybkości gry
        self.speedup_scale=1.1

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        '''Inicjalizacja ustawien ktore ulegają zmianie w trakcie gry'''
        self.dolphin_speed_factor = 1.5
        self.bubble_speed_factor = 3
        self.fisher_speed_factor = 1
        self.fishers_direction = 1

    def increase_speed(self):
        '''Zmiena ustawien dotyczących prędkości'''
        self.dolphin_speed_factor *=self.speedup_scale
        self.bubble_speed_factor *=self.speedup_scale
        self.fisher_speed_factor *=self.speedup_scale

