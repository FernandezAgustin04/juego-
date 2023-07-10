import pygame
from pygame.locals import *

from API.GUI_button_image import *
from API.GUI_form import *
from API.GUI_label import *
from API.GUI_contenedor_nivel import FormContenedorNivel
from manejador_niveles import *

class FormMenuPlay(Form):
    def __init__(self, screen, x, y, w, h, color_background,path_image, color_border="Black", active=True):
        super().__init__(screen, x, y, w, h, color_background, color_border, active)
        self.manejador_niveles = Manejador_niveles(self._master)
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.image = aux_image

        self.label= Label(self._slave,10,50,300,50,"NIVELES","Comic Sans", 45,"white", "")
        self.label_nivel_1 = Label(self._slave,20,270,100,50,"Nivel 1","Comic Sans", 30,"white", "")
        self.label_nivel_2 = Label(self._slave,20,350,100,50,"Nivel 2","Comic Sans", 30,"white", "")
        self.label_nivel_3 = Label(self._slave,20,420,100,50,"Nivel 3","Comic Sans", 30,"white", "")
        self.btn_level_1 = Button_Image(self._slave,x,y,200,270,50,50,r"img\play_icon_134504.png",self.entrar_nivel,"nivel_uno")
        self.btn_level_2 = Button_Image(self._slave,x,y,200,350,50,50,r"img\play_icon_134504.png",self.entrar_nivel,"nivel_dos")
        self.btn_level_3 = Button_Image(self._slave,x,y,200,420,50,50,r"img\play_icon_134504.png",self.entrar_nivel,"nivel_tres")
        self.btn_home = Button_Image(self._slave,x,y,w-70,h-70,50,50,r"API\home.png",self.btn_home_click,"","","Verdana",15,"Green","red","blue")
        
        self.lista_widgets.append(self.label)
        self.lista_widgets.append(self.label_nivel_1)
        self.lista_widgets.append(self.label_nivel_2)
        self.lista_widgets.append(self.label_nivel_3)
        self.lista_widgets.append(self.btn_level_1)
        self.lista_widgets.append(self.btn_level_2)
        self.lista_widgets.append(self.btn_level_3)
        self.lista_widgets.append(self.btn_home)

        self.render()

    def on(self, param):
        print("hola", param)

    def update(self, lista_eventos):
        if self.verificar_dialog_result():
            if self.active:
                self.draw()
                self.render()
                for widgets in self.lista_widgets:
                    widgets.update(lista_eventos)
                    # try:
                    # except:
                    #     print("Error en el funcionamiento del menu del juego")
        else:
            self.hijo.update(lista_eventos)

    def render(self):
        self._slave.blit(self.image,(0,0))
    
    def entrar_nivel(self,nombre_nivel):
        nivel = self.manejador_niveles.get_nivel(nombre_nivel)
        form_contenedor_nivel = FormContenedorNivel(self._master,nivel)
        self.show_dialog(form_contenedor_nivel)

    def btn_home_click(self,param):
        self.end_dialog()



    

