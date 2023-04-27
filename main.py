#Karla Castañeda
#se llama a los módulos respectivos

from tkinter import *
import Sumas
import Llamada_Multi
from tkinter import ttk
import tkinter as tk


#se defines los objetos para ser llamados en el menú principal
def suma2():
    suma1 = Sumas.sumasrapidas(3)
def tablas():
    tabla1 = Llamada_Multi.menu()

#se crea la ventana
root = tk.Tk()
root.title("Interactuar con los niños")
root.geometry("1000x1000")
# Cargar imagen del disco.
image = tk.PhotoImage(file="unnamed.png")
# Insertarla en una etiqueta.
label = ttk.Label(image=image)
label.pack()

#se crea el menú
barramenu = Menu(root)
juegoeduca = Menu(barramenu, tearoff=0)
juegoeduca.add_command(label="Tablas de multiplicar", command=tablas)
juegoeduca.add_command(label="Que tal ágil es tu mente con la suma", command=suma2)
juegoeduca.add_separator()
juegoeduca.add_command(label="Salida", command=root.quit)
barramenu.add_cascade(label="Juegos educativos", menu=juegoeduca)
root.config(menu=barramenu)
root.mainloop()
