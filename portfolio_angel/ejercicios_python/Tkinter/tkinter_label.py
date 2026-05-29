"""
Mostrar texto o imágenes estáticos con los que no se puede interactuar
Sintáxis:
    variableLabel = Label(contenedor-padre, opciones)
"""
from tkinter import *

raiz=Tk()

miFrame=Frame(raiz, width=400, height=400)
miFrame.pack()

miLabel=Label(miFrame, text="Hola Mundo!")
miLabel.place(x=100, y=100) # Lo que hace al sustituir pack por place es que podamos ubicar el texto en cualquier lugar de la interfaz gráfica, evitando el error de que el frame se adapte a su tamaño.

raiz.mainloop()