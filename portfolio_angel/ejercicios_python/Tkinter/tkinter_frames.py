"""
Información sobre tkinter: https://docs.python.org/3/library/tk.html
"""
"""
Trabajando con tkinter raíz
"""

from tkinter import *

raiz = Tk()

raiz.title("Ventana de pruebas")

raiz.resizable(1,1)

# icono = PhotoImage(file="/Users/angel/Proyectos_AWS/portfolio_angel/ejercicios_python/Tkinter/logo.PNG")
# raiz.iconphoto(True, icono)

# raiz.geometry("650x350")

raiz.config(bg="lightyellow")

raiz.config(bd=30)
raiz.config(relief="groove")

raiz.config(cursor="hand2")

miFrame = Frame()

miFrame.pack() # Hay que empaquetarlo; con 'side' lo que hace es anclarlo a algun lado de la raiz = "left", "right",... | con 'anchor' podremos movernos según coordenadas = "n", "s", ... | con 'fill' = x se expanderá según redimensionemos la raíz | con 'fill' = y junto con 'expand' = True, al redimensionar podrá expandirse verticalmente. | Si junto al 'expand' usamos el 'fill' = both se expandera de forma total

miFrame.config(bg="lightblue")
miFrame.config(width=650, height=350) # Para poder cambiar el tamaño hay que quitarle sus medidas fijadas a la raíz.

miFrame.config(bd=20)
miFrame.config(relief="groove")

miFrame.config(cursor="pirate")
raiz.mainloop()