import pygame

class Especial(pygame.sprite.Sprite):
    def __init__(self,x,y, pantalla, imagen) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.pantalla = pantalla
        self.imagen = imagen[0]
        self.escalador_imagen()   
        self.animacion = imagen
        self.rect = self.imagen.get_rect()        
        self.activo = True 
        self.rect.y = y
        self.rect.x = x
        self.accion = 0
    
    def escalador_imagen(self):
        self.imagen = pygame.transform.scale(self.imagen,(60,50))   
    
    def animar(self):
        largo = len(self.animacion)
        if self.accion >= largo:
            self.accion = 0
        self.imagen = self.animacion[self.accion]
        self.escalador_imagen()
        self.accion += 1

    def update(self,slave):
        if self.activo:
            self.animar()
            slave.blit(self.imagen, self.rect)