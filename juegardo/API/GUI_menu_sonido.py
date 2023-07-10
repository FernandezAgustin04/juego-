import pygame
from pygame.locals import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_label import *
from API.GUI_slider import *
from SQL.sql import *

class FormSonido(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border,active,path_image) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border,active)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.image = aux_image

        self.volumen = 0.2
        self.flag_play = True
        self._slave = aux_image

        self._btn_home = Button_Image(self._slave,x,y,w-70,h-70,50,50,r"RECURSOS\boton_settings.png",self.btn_home_click,"","","Verdana",15,"Green","red","blue")

        self.lista_widgets.append(self._btn_home)

        self.label= Label(self._slave,10,50,300,50,"SETTINGS","Comic Sans", 45,"white", "")
        self.label_musica = Label(self._slave,50,200,100,50,"Sonido","Comic Sans", 30,"white", "")
        self.boton_play= Button(self._slave,x,y,150,200,100,50,"Red","blue", self.btn_play_click, "Nombre","Pausa","Comic Sans",25,"White")
        self.label_volume = Label(self._slave,320,380,100,50,"20%","Comic Sans", 30,"white", "")
        self.slider_volumen = Slider(self._slave,x,y,50,400,250,15,self.volumen,"green","green")

        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_musica)
        self.lista_widgets.append(self.boton_play)
        self.lista_widgets.append(self.label_volume)
        self.lista_widgets.append(self.slider_volumen)

        self.render()

    
    def btn_play_click(self,param):
        if self.flag_play:
            pygame.mixer.music.pause()
            self.boton_play._font_color = "White"
            self.boton_play._color_background = "Green"
            self.boton_play.set_text("Play")
        else:
            pygame.mixer.music.unpause()
            self.boton_play._font_color = "White"
            self.boton_play._color_background = "Red"
            self.boton_play.set_text("Pause")
        self.flag_play = not self.flag_play

    def update_volumen(self,lista_eventos):
        self.volumen = self.slider_volumen.value
        self.label_volume.set_text(f"{round(self.volumen *100)}%")
        pygame.mixer.music.set_volume(self.volumen)

    def btn_home_click(self,param):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widgets in self.lista_widgets:
                    try:
                        widgets.update(lista_eventos)
                    except:
                        print("Error en el funcionamiento del juego")
                self.update_volumen(lista_eventos)
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(self.image,(0,0))