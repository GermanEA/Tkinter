import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

# Configurando el grid
ventana.rowconfigure(0, weight=2)
ventana.rowconfigure(1, weight=10)
ventana.columnconfigure(0, weight=1)
ventana.columnconfigure(1, weight=5)


def evento1():
    boton1.config(text='Botón1 presionado')


def evento2():
    boton2.config(text='Botón2 presionado')


def evento3():
    boton3.config(text='Botón3 presionado')


def evento4():
    boton4.config(text='Botón4 presionado', fg='blue', relief=tk.GROOVE, background='yellow')


boton1 = ttk.Button(ventana, text='Botón 1', command=evento1)
boton2 = ttk.Button(ventana, text='Botón 2', command=evento2)
boton3 = ttk.Button(ventana, text='Botón 3', command=evento3)
boton4 = tk.Button(ventana, text='Botón 4', command=evento4)

# N, S, E, W
boton1.grid(row=0, column=0, sticky=tk.NSEW, padx=40, pady=30, ipadx=20, ipady=50, columnspan=2)
boton2.grid(row=1, column=0, sticky='NSEW')
# boton3.grid(row=0, column=1, sticky='NSEW')
boton4.grid(row=1, column=1, sticky='NSEW')

ventana.mainloop()