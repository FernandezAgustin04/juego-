import pygame
from pygame.locals import *
from config import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_menu_sonido import *

class FormContenedorNivel(Form):
    def __init__(self, screen:pygame.Surface, nivel):
        super().__init__(screen,0,0,WIDTH,HEIGHT,"")
        nivel.slave = self._slave
        self.nivel = nivel
        self.btn_home = Button_Image(self._slave,self._x,self._y,self._w-100,self._h-100,50,50,r"API\home.png",self.btn_home_click,"")
        self.lista_widgets.append(self.btn_home)

    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for x in self.lista_widgets:
            try:
                x.update(lista_eventos)
            except:
                print("Error en el selector de niveles del juego")
        self.draw()
    

    def btn_home_click(self,param):
        self.end_dialog()

