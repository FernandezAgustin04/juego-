import pygame
from pygame.locals import *
from nivel import *
from config import *
from slider import *


class NivelUno(Nivel):
    def __init__(self, pantalla) -> None:
        self.pantalla = pantalla
        #FONDO 
        img_fondo = pygame.image.load(r"img/cielo.png")
        img_fondo = pygame.transform.scale(img_fondo, SIZE_SCREEN)

        #ICONO
        icono = pygame.image.load(r"img/personaje_caminando_1.png")
        pygame.display.set_icon(icono)

        correr = [
            pygame.image.load(r"img/personaje_caminando_1.png"),
            pygame.image.load(r"img/personaje_caminando_2.png"),
            pygame.image.load(r"img/personaje_caminando_3.png"),
            pygame.image.load(r"img/personaje_caminando_4.png"),
            pygame.image.load(r"img/personaje_caminando_5.png"),
            pygame.image.load(r"img/personaje_caminando_6.png"),
            pygame.image.load(r"img/personaje_caminando_7.png"),
        ]
        quieto = [
            pygame.image.load(r"img/personaje_quieto_1.png")
        ]
        saltando = [
            pygame.image.load(r"img/personaje_quieto_1.png")
        ]

        lista_acciones = [quieto, correr, saltando]

        personaje_principal = Personaje(pantalla,quieto[0], (20,45), 80, 550, 10, -15, lista_acciones)
        
        #PLATAFORMA 
        piso = plataforma(self.pantalla,r"img\pasto.png", (WIDTH,82),0,HEIGHT-82)

        plataforma_a = plataforma(self.pantalla,r"img\pasto.png", (400,50),0,260)
        plataforma_b = plataforma(self.pantalla,r"img\pasto.png", (700,50),260,430)
        plataforma_c = plataforma(self.pantalla,r"img\pasto.png", (700,50),1040,540)
        plataforma_d = plataforma(self.pantalla,r"img\pasto.png", (260,50),480,315)
        plataforma_e = plataforma(self.pantalla,r"img\pasto.png", (200,50),780,245)
        plataforma_f = plataforma(self.pantalla,r"img\pasto.png", (200,50),1000,200)

        lista_plataformas = [piso, plataforma_a,plataforma_b,plataforma_c,plataforma_d,plataforma_e,plataforma_f]

        #ENEMIGOS
        correr_00 = [
            pygame.image.load(r"img\enemigo_1_caminando_01.png"),
            pygame.image.load(r"img\enemigo_1_caminando_02.png"),
            pygame.image.load(r"img\enemigo_1_caminando_03.png"),
            pygame.image.load(r"img\enemigo_1_caminando_04.png"),
            pygame.image.load(r"img\enemigo_1_caminando_05.png"),
            pygame.image.load(r"img\enemigo_1_caminando_06.png"),
            pygame.image.load(r"img\enemigo_1_caminando_07.png")
        ]
        quieto_00 = [
            pygame.image.load(r"img\enemigo_1_caminando_01.png")
        ]
        enemigo_00_movimientos = [quieto_00,correr_00]

        correr_01 = [
            pygame.image.load(r"img\enemigo_1_caminando_01.png"),
            pygame.image.load(r"img\enemigo_1_caminando_02.png"),
            pygame.image.load(r"img\enemigo_1_caminando_03.png"),
            pygame.image.load(r"img\enemigo_1_caminando_04.png"),
            pygame.image.load(r"img\enemigo_1_caminando_05.png"),
            pygame.image.load(r"img\enemigo_1_caminando_06.png"),
            pygame.image.load(r"img\enemigo_1_caminando_07.png")
        ]
        quieto_01 = [
            pygame.image.load(r"img\enemigo_1_caminando_01.png")
        ]
        enemigo_01_movimientos = [quieto_00,correr_00]
        
        enemigo = Enemigo(pantalla, quieto_00[0],(60,90),530,380,enemigo_00_movimientos,900,260)
        enemigo_01 = Enemigo(pantalla, quieto_01[0],(60,90),530,380,enemigo_01_movimientos,900,260)

        shovel = pygame.image.load("img/shovel.png")
        pala = [
            shovel,
            shovel,
            pygame.transform.flip(shovel,True,False),
            pygame.transform.flip(shovel,True,False)
        ]
        shovel_1 = Especial(80,220,pantalla,pala)
        shovel_2 = Especial(1120,460,pantalla,pala)
        shovel = [shovel_1,shovel_2]

        # CORAZON
        cora = pygame.image.load("img\corazon.png")
        imagen_vida = [
            cora,
            cora,
            pygame.transform.flip(cora,True,False),
            pygame.transform.flip(cora,True,False)
        ]
        corazon = Especial(1100,150,pantalla,imagen_vida)
        corazones = [corazon]

        
        super().__init__(pantalla, personaje_principal, lista_plataformas, img_fondo, enemigo,enemigo_01, shovel, corazones)