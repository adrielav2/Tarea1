from Ficha import *
import random

class Tablero:

    #Defina aquí los atributos de Tablero
    Casillas = 0
    Jugadores = 4
    Turno = 0

    #también va a necesitar una lista de Fichas (puede asumir un número de Fichas fijo si le parece más fácil), 
    #y un mecanismo para saber quién sigue en el turno
    Jugador1 = Ficha("Azul")
    Jugador2 = Ficha("Rojo")
    Jugador3 = Ficha("Amarillo")
    Jugador4 = Ficha("Naranja")
    Orden = [Jugador1,Jugador2,Jugador3,Jugador4]
    random.shuffle(Orden)


    #agregue parámetros necesarios después de self
    #para iniciar los valores de sus atributos
    def __init__(self, Casillas):
        #inicialice aquí todos los atributos
        #no olvide usar self.atributo para acceder el atributo de la clase
        self.Casillas = Casillas


    #defina aquí los métodos de Tablero
    #recuerde que el primer parámetro de cada método es siempre self
  
    def Juego(self):
        while(self.Orden[self.Turno].avanzar() < self.Casillas):
            if(self.Turno == 3):
                self.Turno = 0
            else:
                self.Turno +=1
        print("Gana el jugador " + self.Orden[self.Turno].color)
    



