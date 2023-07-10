import pygame, sys,time
from modo import *
from config import *
from class_jugador import *
from class_enemigo import *
from especiales import *
from class_plataformas import *


class Nivel():
    def __init__(self,pantalla,personaje_principal,lista_plataformas,imagen_fondo,enemigo,enemigo_01,shovel,vidas) -> None:
        self.slave = pantalla
        self.jugador = personaje_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.enemigo = enemigo
        self.enemigo_01 = enemigo_01
        self.shovel = shovel
        self.vidas = vidas
        self.comienzo = time.time()
        

    def leer_inputs(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit(0)
        elif (keys[pygame.K_UP]) and (keys[pygame.K_RIGHT]):
            self.jugador.mover_derecha()
            self.jugador.saltar()
        elif (keys[pygame.K_UP]) and (keys[pygame.K_LEFT]):
            self.jugador.mover_izquierda()
            self.jugador.saltar()
        elif keys[pygame.K_UP]:
            self.jugador.saltar()
        elif keys[pygame.K_RIGHT]:
            self.jugador.mover_derecha()
        elif keys[pygame.K_LEFT]:
            self.jugador.mover_izquierda()
        else:
            self.jugador.quieto()
        if keys[pygame.K_SPACE]:
            ahora = pygame.time.get_ticks()
            if ahora - self.jugador.ultimo_disparo > self.jugador.retrazo_disparo:
                self.jugador.disparar(self.slave)
                self.jugador.ultimo_disparo = ahora
    
    def leer_eventos(self,lista_eventos):
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

    def dibujar_rectangulos(self):
        if get_mode() == True:
            for plataforma in self.plataformas:
                for x in plataforma.rectangulos:
                    pygame.draw.rect(self.slave, "green",x,2)
            for lado in self.jugador.lado_personaje:
                pygame.draw.rect(self.slave, "green",lado,2)

    def actualizar_pantalla(self):
        self.slave.blit(self.img_fondo, (0, 0))

        for platform in self.plataformas:
            platform.update(self.slave)

        self.jugador.update(self.slave, self.plataformas, self.enemigo, self.enemigo_01, self.shovel, self.vidas)

        self.enemigo.update(self.slave, self.jugador)
        self.enemigo_01.update(self.slave, self.jugador)

        for x in self.shovel:
            x.update(self.slave)

        for x in self.vidas:
            x.update(self.slave)

        
        # FUENTE ##############################################################
        fuente = pygame.font.SysFont("Arco Font",70)
        # FORMULARIOS   #########################################################3
        info1 = pygame.Rect(0,0,WIDTH,75)
        pygame.draw.rect(self.slave, "black",info1 ,100)

        tiempo_transcurrido = time.time() - self.comienzo
        if tiempo_transcurrido >= 60:
            self.jugador.esta_vivo = False
            self.jugador.vidas = 0
        else:
            if tiempo_transcurrido > 50:
                tiempo = fuente.render(f"00:0{int(60-tiempo_transcurrido)}", True, "White")
            else:
                tiempo = fuente.render(f"00:{int(60-tiempo_transcurrido)}", True, "White")
            self.slave.blit(tiempo, (500,20))
        score = fuente.render(f"Score:{self.jugador.puntuacion}", True, "White")
        self.slave.blit(score, (912,20))
        self.jugador.mostrar_vidas(self.slave)

    def update(self, lista_eventos):
        if self.jugador.gano:
            win = pygame.image.load(r"img\fondo_win.png")
            win = pygame.transform.scale(win, (WIDTH, HEIGHT))
            self.slave.blit(win, (0, 0))
        elif self.jugador.esta_vivo:
            self.leer_inputs()
            self.leer_eventos(lista_eventos)
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        else:
            lose = pygame.image.load(r"img\fondo_lose.png")
            lose = pygame.transform.scale(lose, (WIDTH, HEIGHT))
            self.slave.blit(lose, (0, 0))

