import pygame
from especiales import Especial

class Slider(Especial):
    def __init__(self,x,y, pantalla, imagen,limite_mayor,limite_menor) -> None:
        super().__init__(x,y, pantalla, imagen)
        self.posicion = "derecha"
        self.limite_mayor = limite_mayor
        self.limite_menor = limite_menor
    
    def escalador_imagen(self):
        self.imagen = pygame.transform.scale(self.imagen,(60,50))   
    
    def animar(self):
        largo = len(self.animacion)
        if self.accion >= largo:
            self.accion = 0
        self.imagen = self.animacion[self.accion]
        self.escalador_imagen()
        self.accion += 1

    def mover(self):
        self.direccion()
        if self.posicion == "derecha":
            self.rect.x += 15
        elif self.posicion == "izquierda":
            self.rect.x -= 15
    
    def direccion(self):
        if self.rect.x >= self.limite_mayor:
            self.posicion = "izquierda"
        elif self.rect.x <= self.limite_menor:
            self.posicion = "derecha"
        
    def update(self,slave):
        if self.activo:
            self.mover()
            self.animar()
            slave.blit(self.imagen, self.rect)