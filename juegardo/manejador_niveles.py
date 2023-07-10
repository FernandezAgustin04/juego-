import pygame
from nivel_uno import *
from nivel_dos import *
from nivel_tres import *

class Manejador_niveles:
    def __init__(self,pantalla) -> None:
        self.slave = pantalla
        self.niveles = {"nivel_uno":NivelUno, "nivel_dos": NivelDos, "nivel_tres": NivelTres}

    def get_nivel(self,nombre_nivel):
        return self.niveles[nombre_nivel](self.slave)