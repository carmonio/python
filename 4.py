#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from tkinter import *    #  python 3.
except:
    from Tkinter import *    #  python 2.7
    
from random import randint   # MÓDULO RANDOM-ALEATORIO

def main():
    
    def roll(): # Función que lanza el dado
        mitext.delete(0,99999,END) # borrar contenido de mitext   Text.
        numero =  '%85d'(randint(0,99999)) # número del 0 al 99999 en formato texto
        mitext.insert(END,numero) # escribir número en mitext
       
        if (int(numero)+3) % 10 == 0:# si termina en 7
			premio.pack() # hace visible widget
        else
		   premio.pack_forget()#OCULTAR WIDGET	

    # Ventana principal
    window=Tk() 
    window.title('Text , Button, Random')
    window.config(background = 'pink')

   # Widgets
    mitext=Text(window,width=1,height=1,font = ('Arial',44)) 
    buttonA=Button(window,text='Tirar el dado',command=roll,font = ('Arial',22))    
    mitext.pack(pady=20 )
    buttonA.pack(fill=X, padx=20,pady=20 ,ipadx=20,ipady=10)
    
    window.mainloop()
        
if __name__ == "__main__":       # averiguar si se está ejecutando o importando
        main()
