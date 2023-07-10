import pygame
from pygame.locals import *
from config import*
from API.GUI_button import *
from API.GUI_slider import *
from API.GUI_textbox import *
from API.GUI_label import *
from API.GUI_form import *
from API.GUI_form_menu_score import *
from API.GUI_checkbox import *
from API.GUI_picture_box import *
from API.GUI_form_menu_play import *
from API.GUI_menu_sonido import *


class FormPrueba(Form):
    def __init__(self, screen, x, y, w, h, color_background="red", color_border="black", border_size=-1, active=True) -> None:
        super().__init__(screen, x, y, w, h, color_background, color_border, border_size, active)
        aux_image = pygame.image.load(r"img\fondo_inicio.png")
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self.image = aux_image
        self.volumen = 0.2
        self.mensaje_antiguo = ""

        pygame.mixer.init()

        # CONTROLES ###############################################

        self.ingreso_nombre = Label(self._slave,50,300,220,75,"Ingrese su nombre","Comic Sans", 25,"white", "")
        self.textbox = TextBox(self._slave,x,y,280,320,170,40,"white","gray","red","green",2,"Comic Sans",15,"black")
        self.buscar_posiciones = Label(self._slave,50,485,220,75,"Posiciones","Comic Sans", 25,"white", "")
        self.boton_tabla = Button_Image(self._slave,x,y,280,500,50,50,r"API\Menu_BTN.png",self.btn_tabla_click,"fghj")
        self.buscar_settings = Label(self._slave,50,405,220,75,"Settings","Comic Sans", 25,"white", "")
        self.boton_settings = Button_Image(self._slave,x,y,280,420,50,50,r"API\Menu_BTN.png",self.btn_settings_click,"fghj")
        self.label_jugar = Label(self._slave,100,580,200,75,"A JUGAR!!","Comic Sans", 25,"white", "")
        self.boton_jugar = Button_Image(self._slave,x,y,300,580,140,75,r"img\play_icon_134504.png",self.btn_jugar_click,"a")

        # AGREGAR #############################
        self.lista_widgets.append(self.ingreso_nombre)
        self.lista_widgets.append(self.buscar_posiciones)
        self.lista_widgets.append(self.buscar_settings)
        self.lista_widgets.append(self.textbox)
        self.lista_widgets.append(self.boton_tabla)
        self.lista_widgets.append(self.boton_jugar)
        self.lista_widgets.append(self.label_jugar)
        self.lista_widgets.append(self.boton_settings)
        pygame.mixer.music.load("musica_fondo.mp3")
        pygame.mixer.music.set_volume(self.volumen)
        pygame.mixer.music.play(-1)

        self.render()
    
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
        else:
            self.hijo.update(lista_eventos)

    def ingreso_txt_box(self):
        return self.textbox.get_text()

    def render(self):
        self._slave.blit(self.image,(0,0))

    def btn_jugar_click(self,param):
        frm_jugar = FormMenuPlay(self._master,250,80,700,550,MAGENTA,r"img\fondo_inicio.png",WHITE,True)
        self.show_dialog(frm_jugar)

    def btn_settings_click(self,texto):
        form_sonido = FormSonido(self._master,250,80,700,550,"Green","White",True,r"img\fondo_inicio.png")
        self.show_dialog(form_sonido)
    
    def btn_tabla_click(self,texto):
        form_puntaje = FormMenuScore(self._master,340,30,500,650,"Green","White",True,r"img\fondo_inicio.png",
                                    "dic_score",100,10,10)

        self.show_dialog(form_puntaje)