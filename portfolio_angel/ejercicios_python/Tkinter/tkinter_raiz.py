"""
Información sobre tkinter: https://docs.python.org/3/library/tk.html
"""
"""
Trabajando con tkinter raíz
"""

from tkinter import *

raiz = Tk() # Se le suele llamar así por convención

raiz.title("Ventana de pruebas")

raiz.resizable(1,1) # Debemos meter width y eight. Parámetros de tipo booleano. (0,0) = no se puede cambiar el tamaño. (1,1) = se puede redimensionar a lo alto y ancho. Debemos jugar con estos valores.

icono = PhotoImage(file="/Users/angel/Proyectos_AWS/portfolio_angel/ejercicios_python/Tkinter/logo.PNG")
raiz.iconphoto(True, icono)

raiz.geometry("650x350")

raiz.config(bg="yellow") # Nos permite establecer diferentes características.

raiz.mainloop() # Es un bucle infinito básicamente, para poder estar a la escucha de eventos. Debe estar siempre al final.