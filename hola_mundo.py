import tkinter as tk
from tkinter import ttk

# Creamos un objeto de la clase Tk
ventana = tk.Tk()

# Moficiamos el tamaño de la ventana (pixeles) y el título
ventana.geometry('600x400')
ventana.title('Hola Mundo')

# Cambiando el icono
ventana.iconbitmap('icono.ico')


# Botón (widget), el objeto padre es la ventana
def evento_click():
    boton1.config(text='Presionado')
    boton2 = ttk.Button(ventana, text='Dar click 2')
    boton2.pack()
    print('Pulsando botón')


boton1 = ttk.Button(ventana, text='Dar click', command=evento_click)

# Utilizar el pack layout manager para mostrar el botón de la ventana
boton1.pack()

# Iniciamos la vetana (esta línea la ejecutamos al final)
ventana.mainloop()