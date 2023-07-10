import pygame,random
from class_jugador import Personaje
from proyectil import Disparo
from config import *

class Enemigo(Personaje):
    def __init__(self, pantalla, imagen, size: tuple, x, y,acciones,limite_mayor, limite_menor, vidas=1) -> None:
        super().__init__(pantalla, imagen, size, x, y, 10, 0, acciones)
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor
        self.retrazo = 1000
        self.ultimo_disparo = pygame.time.get_ticks()
        self.ultima_direccion = pygame.time.get_ticks()
        self.esta_vivo = True
        self.muerte_1 = False
        self.vidas = vidas

    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
        else:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultima_direccion > self.retrazo:
                self.ultima_direccion = ahora
                random_number = random.randint(0, 1)
                if random_number == 0:
                    self.posicion = "izquierda"
                else:
                    self.posicion = "derecha"

    def mover(self):
        if self.esta_vivo:
            self.direccion()
            if self.posicion == "derecha":
                super().mover_derecha()
            elif self.posicion == "izquierda":
                super().mover_izquierda()
    
    def collision(self,personaje):
        for x in personaje.lista_proyectiles:
            if x.disparo_rect.colliderect(self.rect):
                self.vidas -= 1
                personaje.lista_proyectiles.remove(x)
    
    def disparar(self,slave):
        bala = Disparo(self.rect.x,self.rect.y,slave,r"RECURSOS\bola de fuego.png", self.posicion)
        pygame.mixer.Sound(r"RECURSOS\disparo.wav").play().set_volume(0.5)
        self.lista_proyectiles.append(bala)

    def muerte(self):
        if self.vidas <= 0:
            self.esta_vivo = False

    def update(self,slave):
        self.muerte()
        if self.esta_vivo == True:
            ahora = pygame.time.get_ticks()
            if ahora - self.ultimo_disparo > (self.retrazo * 2):
                self.disparar(slave)
                self.ultimo_disparo = ahora
            self.mover()
            slave.blit(self.imagen, self.rect)
            for x in self.lista_proyectiles:
                x.trayectoria()
                x.update()
                if x.disparo_rect.left == WIDTH or 0:
                    self.lista_proyectiles.remove(x)
        else:
            if self.muerte_1:
                self.rect = None
            else:
                pygame.mixer.Sound(r"RECURSOS\ruido_muerte.wav").play()
                self.rect = None
                self.muerte_1 = True

