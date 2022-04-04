import random
import numpy as np
from Game import window,start,menu
from Tablero import tablero

class Barco:
    nro= 0
    def __init__(self, nombre: str,tamaño: int,tablero):
        Barco.nro= Barco.nro+1
        self._nombre= nombre
        self._tamaño= tamaño
        self._nro= Barco.nro
        self.ubicar(tablero)

    def getSize(self):
        return self._tamaño
    def getName(self):
        return self._nombre
    def getNro(self):
        return self._nro
    def ubicar(self, tablero ):
        if self.getName()=='Submarino':
            x= random.randint(0,9)
            y= random.randint(0,9)
            tablero.setTablero(x,y,1)
        elif self.getName()=='Destructor':
            x= random.randint(0,8)
            y= random.randint(0,8)
            v= random.randint(0,1)
            if v==0:
                tablero.setTablero(x,y,2)
                tablero.setTablero(x+1,y,2)
            else:
                tablero.setTablero(x,y,2)
                tablero.setTablero(x,y+1,2)
        elif self.getName()=='Crucero':
            x= random.randint(0,7)
            y= random.randint(0,7)
            v= random.randint(0,1)
            if v==0:
                tablero.setTablero(x,y,3)
                tablero.setTablero(x+1,y,3)
                tablero.setTablero(x+2,y,3)
            else:
                tablero.setTablero(x,y,3)
                tablero.setTablero(x,y+1,3)
                tablero.setTablero(x,y+2,3)
        else:
            x= random.randint(0,6)
            y= random.randint(0,6)
            v= random.randint(0,6)
            if v==0:
                tablero.setTablero(x,y,4)
                tablero.setTablero(x+1,y,4)
                tablero.setTablero(x+2,y,4)
                tablero.setTablero(x+3,y,4)
            else:
                tablero.setTablero(x,y,4)
                tablero.setTablero(x,y+1,4)
                tablero.setTablero(x,y+2,4)
                tablero.setTablero(x,y+3,4)


Jugador1= tablero(False)#tablero del enemigo
Enemigo= tablero(True)#tablero en el que juega el enemigo(mapa del jugador 1)
BatallaNavalMenu= start()
Run=True
while Run:
    if BatallaNavalMenu.out and BatallaNavalConfig.out:
        Submarinos1=[]
        Destructores1=[]
        Cruceros1=[]
        portaviones1=[]
        for i in range(0,BatallaNavalConfig.submarinos):
            submarino=Barco("Submarino",1,Enemigo)
            submarinoe=Barco("Submarino",1,Jugador1)
        for i in range(0,BatallaNavalConfig.destructores):
            destructor= Barco("Destructor",2,Enemigo)
            destructore= Barco("Destructor",2,Jugador1)
        for i in range(0,BatallaNavalConfig.cruceros):
            crucero= Barco("Crucero",3,Enemigo)
            cruceroe= Barco("Crucero",3,Jugador1)
        for i in range(0,BatallaNavalConfig.portaviones):
            portavion= Barco("Portaviones",4,Enemigo)
            portavione= Barco("Portaviones",4,Jugador1)

        BatallaNaval= window()
        BatallaNaval.run(Jugador1,Enemigo)
        break
    else:
        BatallaNavalMenu= start() 
        BatallaNavalMenu.run()
        if(BatallaNavalMenu.out):    
            BatallaNavalConfig= menu()
        else:
            break

