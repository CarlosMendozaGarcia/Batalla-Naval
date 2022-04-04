import tkinter as tk
from tkinter import font, messagebox
import pygame as pyg
import numpy as np
import random
white= 255,255,255
black= 0,0,0

#principal clase para el juego
class window:
    width=1200
    height= 700
    size= width,height
    Ship= pyg.image.load('ship.png')
    cross= pyg.image.load('equis.png')
    bg= pyg.image.load('Background.jpg')
    bg= pyg.transform.scale(bg,(1200,700))

    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode(self.size)
        pyg.display.set_caption("Batalla Naval")
        pyg.display.set_icon(self.Ship)
        self.turno=1
    def run(self,tablero1,tablero2):
        run= True
        while run:
            for event in pyg.event.get():
                if event.type == pyg.QUIT: run=False
                if event.type == pyg.MOUSEBUTTONUP: #si el usuario hace click a la ventana
                    x, y = pyg.mouse.get_pos()
                    if (x>=50) and (x<=550) and (y>100) and (y<600): #se asegura que el mouse se encuentre en el tablero
                        #los siguientes dos ciclos los utiliza para saber en que recuadro del tablero dio click mediante 
                        #el uso de distancia euclidiana entre 2 puntos
                        min= 100000000
                        for i in range(0,10):
                            for j in range(0,10):
                                left= tablero1.getCoordenadas(i,j)[0]
                                top= tablero1.getCoordenadas(i,j)[1]
                                d= np.sqrt((left-x)**2+(top-y)**2)
                                if d < min:
                                    min=d
                                    I=i                            
                                    J=j
                        #comienza a realizar los cambios en el tablero
                        if tablero1.getTablero(I,J)>0: #el jugador atino a un barco
                            tablero1.setTablero(I,J,-1)
                            #realiza su movimiento el bot
                            x= random.randint(0,9)
                            y= random.randint(0,9)
                            if tablero2.getTablero(x,y)>0: #el bot/la maquina le atino a un barco
                                tablero2.setTablero(x,y,-1)
                            elif tablero2.getTablero(x,y)==0:# el bot no le atino a un barco
                                tablero2.setTablero(x,y,-2)
                            self.turno=self.turno+1 #aumenta el turno
                        elif tablero1.getTablero(I,J)==0: # el jugador no le atino a un barco
                            tablero1.setTablero(I,J,-2)
                            x= random.randint(0,9)
                            y= random.randint(0,9)
                            if tablero2.getTablero(x,y)>0:
                                tablero2.setTablero(x,y,-1)
                            elif tablero2.getTablero(x,y)==0:
                                tablero2.setTablero(x,y,-2)
                            self.turno=self.turno+1
                        #proceso para terminar el progra
                        if self.perder():
                            run= False
            #metodo para realizar todo detalle grafico
            self.base(tablero1,tablero2)
        self.quit()
    #realiza tanto el fondo, como las diferentes lineas y mensajes que sean necesarios en la ventana
    def base(self,tablero1,tablero2):
        self.screen.blit(self.bg,(0,0))
        font= pyg.font.Font('Fixedsys.ttf',32)
        title1=font.render('Mapa enemigo',True,(0,0,0),None)
        title2= font.render('Su Mapa',True,(0,0,0),None)
        title1Rect=title1.get_rect()
        title2Rect=title2.get_rect()
        title1Rect.topleft=(50,50)
        title2Rect.topleft=(650,50)
        self.screen.blit(title1,title1Rect)
        self.screen.blit(title2,title2Rect)
        self.Board(tablero1,False)
        self.Board(tablero2,True)
        pyg.display.flip()
    def quit(self):
        pyg.quit()
    #dibuja los tableros, si enemigo es igual a Falso, debe dibujar el tablero del jugador
    def Board(self,tablero,enemigo):
        if not enemigo:
            tleft=50
            topright=50,100
            topleft=550,100
            bottomright=50,600
            bottomleft=550,600
        else:
            tleft=650
            topright=650,100
            topleft=1150,100
            bottomright=650,600
            bottomleft=1150,600
        pyg.draw.rect(self.screen,white,pyg.Rect(tleft,100,500,500))
        pyg.draw.line(self.screen,black,topright,topleft,3)
        pyg.draw.line(self.screen,black,bottomright,bottomleft,3)
        pyg.draw.line(self.screen,black,topright,bottomright,3)
        pyg.draw.line(self.screen,black,topleft,bottomleft,3)
        #realiza el tablero y a su vez va dibujando todos los cambios que se presenten en la matriz que ubica los barcos
        for i in range (0,10):
            for j in range(0,10):
                left= tablero.getCoordenadas(i,j)[0]
                top= tablero.getCoordenadas(i,j)[1]
                if tablero.getTablero(i,j)>0:
                    if enemigo:
                        pyg.draw.rect(self.screen, (85, 120, 255), pyg.Rect(left-25,top-25,50,50))
                elif tablero.getTablero(i,j)==-1:
                    ncross= pyg.transform.scale(self.cross,(50,50))
                    ncrossRect= ncross.get_rect()
                    ncrossRect.left,ncrossRect.top= left-25,top-25
                    self.screen.blit(ncross,ncrossRect)
                elif tablero.getTablero(i,j)==-2:
                    pyg.draw.circle(self.screen,black,(left,top),10)
                pyg.draw.line(self.screen, black, (left+25,100),(left+25,self.height-100),3)#lineas verticales
                pyg.draw.line(self.screen, black,(tleft,top+25),(tleft+500,top+25),3)#lineas horizontales
    def perder(self):
        if self.turno==100:
            return True
        else:
            return False
        


#permite el inicio del juego
class start():
    width=1200
    height= 700
    size= width,height
    Ship= pyg.image.load('ship.png')
    bg= pyg.image.load('Menu_bg.jpg')
    bg= pyg.transform.scale(bg,(1200,700))
    out=False
    def __init__(self):
        pyg.init()
        self.screen = pyg.display.set_mode(self.size)
        pyg.display.set_caption("Batalla Naval")
        pyg.display.set_icon(self.Ship)
    def run (self):
        run= True
        font=pyg.font.Font('Fixedsys.ttf',100)#estilo de letra utilizado en el programa
        font2=pyg.font.Font('Fixedsys.ttf',50)
        text=font.render('BATALLA NAVAL',True,(0,0,0),None)
        text2= font2.render('Empezar',True,(0,0,0),None)
        textrect= text.get_rect()
        button= text2.get_rect()
        textrect.center=(self.width/2,self.height/2)
        button.center=(self.width/2,self.height/2+200)
        #mientras el ciclo se mantenga activo se realiza cada linea
        while run:
            for event in pyg.event.get():
                if event.type == pyg.QUIT: run= False
                if event.type == pyg.MOUSEBUTTONUP: #si el usuario da click en la ventana
                    x,y = pyg.mouse.get_pos()
                    if(x>=button.left) and (x<=button.left+button.width) and (y>=button.top) and (y<=button.top+button.height): #validación del boton
                        run=False
                        self.out=True
            
            self.screen.blit(self.bg,(0,0))
            pyg.draw.rect(self.screen,(255,255,255),textrect)
            pyg.draw.rect(self.screen,(134,160,173),button)
            self.screen.blit(text,textrect)
            self.screen.blit(text2,button)
            pyg.display.flip()
        self.quit()
    #sale del programa
    def quit(self):
        pyg.quit()
        
#hace la ventana de configuración del juego (pide el numero de barcos)
class menu:
    out=False
    def __init__(self):
        self.menu= tk.Tk()
        self.menu.config(width=1200,height=700)
        self.menu.title('Batalla Naval')
        self.ship= tk.PhotoImage(file='ship.png')
        self.font=font.Font(family='Fixedsys',size=32)
        self.menu.iconphoto(False,self.ship)
        self.run()
        self.menu.mainloop()
    def run(self):
        #introduce strings a la ventana
        mbg= tk.Canvas(self.menu,width=1200,height=700)
        mbg.create_text(500,50,text='Numero de submarinos que desea:',fill="black",font=self.font)
        mbg.create_text(500,200,text='Numero de destructores que desea:',fill="black",font=self.font)
        mbg.create_text(500,350,text='Numero de crueceros que desea:',fill="black",font=self.font)
        mbg.create_text(500,500,text='Numero de portaviones que desea:',fill="black",font=self.font)
        mbg.pack()
        #inicializa y ubica las entradas del sistema
        self.Text_1= tk.Entry(self.menu,None,borderwidth= 2,font=self.font,width=10)#nro de subsmarinos
        self.Text_1.place(x=100,y=100)
        self.Text_2=tk.Entry(self.menu,None,borderwidth= 2,font=self.font,width=10)#nro de destructores
        self.Text_2.place(x=100,y=250)
        self.Text_3=tk.Entry(self.menu,None,borderwidth= 2,font=self.font,width=10)#nro de cruceros
        self.Text_3.place(x=100,y=400)
        self.Text_4=tk.Entry(self.menu,None,borderwidth= 2,font=self.font,width=10)#nro de portaviones
        self.Text_4.place(x=100,y=550)
        #inicializa y ubica el boton para empezar el juego
        Boton= tk.Button(self.menu,text='Empezar',
        command= self.verificarText , #comando a realizar al momento de oprimir
        font= self.font)
        Boton.place(x=900,y=200)
    #permite verificar si los nros de barcos no excede el tamaño original del juego
    def verificar(self):
        if(self.submarinos<=4) and (self.destructores<=3) and (self.cruceros<=2) and (self.portaviones<=1) :
            if (self.submarinos<=0) and (self.destructores<=0) and (self.cruceros<=2) and (self.portaviones<=0):
                messagebox.showinfo(title="Batalla Naval",message='no introducio barcos')
            else:
                self.menu.destroy()
                self.out=True
        else:
            messagebox.showinfo(title="Batalla Naval",message='el numero de barcos es mayor al esperado')
    #validaciones de las entradas
    def verificarText(self):
        if(self.Text_1.get()==''):
            self.submarinos=0
        else:
            self.submarinos=int(self.Text_1.get())
        
        if(self.Text_2.get()==''):
            self.destructores=0
        else:
            self.destructores=int(self.Text_2.get())

        if(self.Text_3.get()==''):
            self.cruceros=0
        else:
            self.cruceros=int(self.Text_3.get())

        if(self.Text_4.get()==''):
            self.portaviones=0
        else:
            self.portaviones=int(self.Text_4.get())
        #verifica antes de mandar el juego
        self.verificar()


