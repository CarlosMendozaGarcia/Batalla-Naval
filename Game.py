import pygame as pyg
import numpy as np
white= 255,255,255
black= 0,0,0

#principal clase para el juego
class window():
    height=600
    width=800
    size= width, height
    Ship= pyg.image.load('ship.png')
    Shiprect= Ship.get_rect()

    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode(self.size)
        pyg.display.set_caption("Batalla Naval")
        pyg.display.set_icon(self.Ship)
        self.turno=1
    def run(self,tablero):
        run= True
        if self.turno%2==1:
            pyg.display.set_caption("Batalla Naval-Jugador 1")
        else:
            pyg.display.set_caption("Batalla Naval-Jugador 2")
        while run:
            for event in pyg.event.get():
                if event.type == pyg.QUIT: run=False
                if event.type == pyg.MOUSEBUTTONUP:
                    x, y = pyg.mouse.get_pos()
                    min= 100000
                    for i in range(0,10):
                        for j in range(0,10):
                            left= tablero.getCoordenadas(i,j)[0]
                            top= tablero.getCoordenadas(i,j)[1]
                            d= np.sqrt((left-x)**2+(top-y)**2)
                            if d < min:
                                min=d
                                I=i                            
                                J=j
                    if tablero.getTablero(I,J)>0: #atino a un barco
                        tablero.setTablero(I,J,-1)
                    else: #no le atino a ningun barco
                        tablero.setTablero(I,J,-2)
                    run= False         
            self.base(tablero)
        self.turno=self.turno+1
        self.quit()
    def base(self,tablero):
        self.screen.fill(white)
        for i in range (0,10):
            for j in range(0,10):
                left= tablero.getCoordenadas(i,j)[0]
                top= tablero.getCoordenadas(i,j)[1]
                if tablero.getTablero(i,j)>0:
                    pyg.draw.rect(self.screen, (85, 120, 255), pyg.Rect(left-35,top-25,70,50))
                elif tablero.getTablero(i,j)==-1:
                    self.Shiprect.update(left,top,10,10)
                elif tablero.getTablero(i,j)==-2:
                    pyg.draw.circle(self.screen,black,(left,top),10)
                pyg.draw.line(self.screen, black, (left+40,0),(left+40,self.height),3)
                pyg.draw.line(self.screen, black,(0,top+30),(self.width,top+30),3)
        pyg.display.flip()
    def quit(self):
        pyg.quit