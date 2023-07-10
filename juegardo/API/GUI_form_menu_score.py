import pygame
from pygame.locals import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_label import *
from SQL.sql import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image,
                score,margen_y,margen_x, espacio) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border,active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))

        self._slave = aux_image
        self.score = score

        self.magen_y = margen_y

        self._btn_home = Button_Image(self._slave,x,y,w-70,h-70,50,50,r"RECURSOS\boton_settings.png",self.btn_home_click,"","","Verdana",15,"Green","red","blue")

        self.lista_widgets.append(self._btn_home)
        
        label_jugador = Label(self._slave, x=margen_x + 10, y = 20, w=w/2-margen_x-10, h=50, text="jugador", 
                        font="Verdana", font_size=30,font_color="White",path_image= r"API\bar.png")
        label_personaje = Label(self._slave, x=margen_x + 10 + w/2-margen_x-10, y=20, w=w/2-margen_x-10, h=50, 
                                text="Puntaje",font="Verdana", font_size=30,font_color="White",path_image= r"API\bar.png")
        
        self.lista_widgets.append(label_jugador)
        self.lista_widgets.append(label_personaje)


        pos_inicial_y = margen_y

        self.score = ver_puntuacion()
        
        for lista in self.score:
            pos_inicial_x = margen_x
            for x in lista:
                cadena = ""
                cadena = f"{x}"
                jugador = Label(self._slave,pos_inicial_x,pos_inicial_y, w/2-margen_x,100, cadena,"Verdana",30,"White","API\Table.png")
                self.lista_widgets.append(jugador)
                pos_inicial_x += w/2 - margen_x
            pos_inicial_y += 100 + espacio

    def btn_home_click(self,param):
        self.end_dialog()

    def update(self,lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                try:
                    wid.update(lista_eventos)
                except:
                    print("Error en el funcionamiento de la pantalla score del juego")
            self.draw()
