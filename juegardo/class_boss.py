import pygame
import random
from class_jugador import Personaje
from class_proyectil import *
from config import *

class Boss(Personaje):
    def __init__(self, pantalla, imagen, size: tuple, x, y, acciones, limite_mayor, limite_menor, vidas=3):
        super().__init__(pantalla, imagen, size, x, y, 10, 0, acciones)
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor
        self.vidas = vidas
        self.esta_vivo = True
        self.retrazo = 1000  # Retraso entre disparos
        self.ultimo_disparo = pygame.time.get_ticks()

    def mover(self):
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

    def disparar(self):
        ahora = pygame.time.get_ticks()
        if ahora - self.ultimo_disparo > self.retrazo:
            self.ultimo_disparo = ahora

            # Disparo hacia arriba
            disparo_arriba = Disparo(self.rect.centerx, self.rect.centery, self.pantalla, "imagen_disparo.png", "arriba")
            self.lista_proyectiles.append(disparo_arriba)

            # Disparo hacia abajo
            disparo_abajo = Disparo(self.rect.centerx, self.rect.centery, self.pantalla, "imagen_disparo.png", "abajo")
            self.lista_proyectiles.append(disparo_abajo)

            # Disparo hacia la izquierda
            disparo_izquierda = Disparo(self.rect.centerx, self.rect.centery, self.pantalla, "imagen_disparo.png", "izquierda")
            self.lista_proyectiles.append(disparo_izquierda)

            # Disparo hacia la derecha
            disparo_derecha = Disparo(self.rect.centerx, self.rect.centery, self.pantalla, "imagen_disparo.png", "derecha")
            self.lista_proyectiles.append(disparo_derecha)

    def update(self):
        super().update()

        if self.esta_vivo:
            self.mover()
            self.disparar()

            # Actualizar la trayectoria de los proyectiles
            for proyectil in self.lista_proyectiles:
                proyectil.trayectoria()
                proyectil.update()

                # Eliminar los proyectiles que salen de la pantalla
                if proyectil.rect.left > WIDTH or proyectil.rect.right < 0 or proyectil.rect.top > HEIGHT or proyectil.rect.bottom < 0:
                    self.lista_proyectiles.remove(proyectil)

        else:
            # Acciones cuando el jefe muere
            pass
