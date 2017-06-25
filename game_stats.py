class GameStats():
    def __init__(self,dolphingame_settings):

        '''Monitorowanie danych statystycznych w grze'''
        self.dolphingame_settings = dolphingame_settings
        self.reset_stats()
        self.game_active=True

    def reset_stats(self):
        '''Inicjalizacja danych statystycznych które mogą zmieniać się w trakcie gry'''


        self.dolphins_left=self.dolphingame_settings.dolphin_limit