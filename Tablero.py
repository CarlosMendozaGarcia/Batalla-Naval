import numpy as np

class tablero:
    def __init__(self,enemigo):
        self.matriz=np.zeros((10,10), dtype= int)
        self.coordenadas= np.zeros((10,10), dtype= tuple)
        if not enemigo:    
            for i in range(0,10):
                for j in range(0,10):
                    self.coordenadas[i][j]=[50+25*(2*j+1),100+25*(2*i+1)]
        else:
            for i in range(0,10):
                for j in range(0,10):
                    self.coordenadas[i][j]=[650+25*(2*j+1),100+25*(2*i+1)]
    def getTablero(self, i: int, j: int):
        return self.matriz[i][j]
    def getCoordenadas(self, i: int, j: int):
        return self.coordenadas[i][j]
    def setTablero(self, i: int, j:int, nro: int):
        self.matriz[i][j]=nro
        