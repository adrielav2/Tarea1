from Dado import *

class Ficha:
    color = ""
    posicion = 0

    dado = Dado(6)
    
    
    def __init__(self, color):
        self.color = color
        self.posicion = 0
    
    def avanzar(self):
        pasos = self.dado.lanzar()
        self.posicion += pasos
        print(self.color)
        print(self.posicion)
        return(self.posicion)
    