import pygame
from config import *

class Disparo(pygame.sprite.Sprite):
    def __init__(self,x,y, pantalla, path,direccion) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pantalla = pantalla
        self.imagen = pygame.image.load(path) 
        self.imagen = pygame.transform.scale(self.imagen,(50,30))   
        self.disparo_rect = self.imagen.get_rect()        
        self.disparo_activo = True 
        self.disparo_rect.top = y
        self.disparo_rect.left = x
        self.velocidad = 20
        self.direccion = direccion

    def trayectoria(self):
        if self.disparo_activo:
            if self.direccion == "derecha" and self.disparo_rect.left < WIDTH:
                self.disparo_rect.left = self.disparo_rect.left + self.velocidad
            elif self.direccion == "izquierda":
                self.disparo_rect.left = self.disparo_rect.left - self.velocidad
            else:
                self.disparo_activo = False 

    def update(self):
        if self.disparo_activo:
            if self.direccion == "izquierda":
                imagen = pygame.transform.flip(self.imagen, True, False)
                self.pantalla.blit(imagen, self.disparo_rect)
            else:
                self.pantalla.blit(self.imagen, self.disparo_rect)