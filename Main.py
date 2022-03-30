import random
import numpy as np
from Game import window
from Tablero import tablero

#clase barco
class Barco:
    nro= 0
    def __init__(self, nombre: str,tamaño: int):
        Barco.nro= Barco.nro+1
        self._nombre= nombre
        self._tamaño= tamaño
        self._nro= Barco.nro

    def getSize(self):
        return self._tamaño
    def getName(self):
        return self._nombre
    def getNro(self):
        return self._nro
    def ubicar(self, tablero: np.array ):
        x= random

Board1= tablero()
Board2= tablero()
BatallaNaval= window()
#turno= BatallaNaval.turno
while BatallaNaval.turno <=10:
    if BatallaNaval.turno%2==1:
        BatallaNaval.run(Board1)
    else:
        BatallaNaval.run(Board2)
BatallaNaval.quit()

