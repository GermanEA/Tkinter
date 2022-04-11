import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

# width cantidad de caracteres que entran en la caja
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER)
entrada1.grid(row=0, column=0)
entrada1.insert(0, 'Introduce una cadena')
entrada1.insert(5, '-')

ventana.mainloop()