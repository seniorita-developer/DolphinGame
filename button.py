import pygame.font

class Button():

    def __init__(self,dolpingame_settings,screen,msg):
        '''Inicjalizacja atrybutów przycisku'''
        self.screen=screen
        self.screen_rect=screen.get_rect()

        #Zdefiniowanie wymiarów i właściwości przycisku
        self.width,self.height=200,50
        self.button_color=(0,255,0)
        self.text_color=(255,255,255)
        self.font=pygame.font.SysFont(None,48)

        #Utworzenie prostokąta przycisku
        self.rect=pygame.Rect(0,0,self.width,self.height)
        self.rect.center=self.screen_rect.center

        self.prepare_msg(msg)

    def prepare_msg(self,msg):
        '''Umieszczenie komunikatu w wygenerowanym obrazie i wyśrodkowanie tekstu na przycisku'''
        self.msg_image=self.font.render(msg,True,self.text_color,self.button_color)
        self.msg_image_rect=self.msg_image.get_rect()
        self.msg_image_rect.center=self.rect.center

    def draw_button(self):
        #Wyświetlenie przycisku z komunikatem
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)

