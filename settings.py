class Settings():
    '''Klasa do przechowywania wszystkich ustawień gry'''

    def __init__(self):
        #Ustawienia ekranu
        self.screen_width=1200
        self.screen_height=650
        self.bg_color=(0,100,255)

        self.dolphin_speed_factor=1.5
        self.dolphin_limit=4
        self.bubble_speed_factor = 3
        self.bubble_width = 6
        self.bubble_height = 6
        self.bubble_color = 255, 0, 0
        self.bubble_allowed = 5

        self.fisher_speed_factor=1
        self.fishers_drop_speed=10

        self.fishers_direction=1



