import tkinter as tk
from tkinter import ttk, messagebox

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de componentes')
ventana.iconbitmap('icono.ico')

entrada1_var = tk.StringVar(value='Valor por default')
entrada1 = ttk.Entry(ventana, width=30, textvariable=entrada1_var)
entrada1.grid(row=0, column=0)

# Etiqueta (label)
etiqueta1 = tk.Label(ventana, text='Aquí se mostrará el contenido de la caja de texto')
etiqueta1.grid(row=1, column=0, columnspan=2)


def enviar():
    # Modificamos el texto de label
    etiqueta1.config(text=entrada1.get())
    # Messagebox
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Info', mensaje1 + ' Informativo')
        messagebox.showerror('Error', mensaje1 + ' Error')
        messagebox.showwarning('Warning', mensaje1 + ' Warning')


# Creamos un botón para recoger los datos
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()