import sys
import tkinter as tk
from tkinter import ttk, messagebox, Menu

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
    etiqueta1.config(text=entrada1.get())
    mensaje1 = entrada1.get()
    if mensaje1:
        messagebox.showinfo('Info', mensaje1 + ' Informativo')


def salir():
    ventana.quit()
    ventana.destroy()
    sys.exit()


def crear_menu():
    # Configurar el menú principal
    menu_principal = Menu(ventana)
    # teoroff = False -> para que no se separe el menú de la interface gráfica
    submenu_archivo = Menu(menu_principal, tearoff=0)
    # Agregamos una nueva opción
    submenu_archivo.add_command(label='Nuevo', command=enviar)
    # Agregar un separador
    submenu_archivo.add_separator()
    # Agregamos la opción de salir
    submenu_archivo.add_command(label='Salir', command=salir)
    # Agregamos el submenú al principal
    menu_principal.add_cascade(menu=submenu_archivo, label='Archivo')
    # Submenu ayuda
    submenu_ayuda = Menu(menu_principal, tearoff=0)
    submenu_ayuda.add_command(label='Acerca de')
    menu_principal.add_cascade(menu=submenu_ayuda, label='Ayuda')
    # Mostramos el menú en la ventana principal
    ventana.config(menu=menu_principal)


# Creamos un botón para recoger los datos
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

crear_menu()
ventana.mainloop()