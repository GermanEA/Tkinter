import tkinter as tk
from tkinter import ttk

ventana = tk.Tk()
ventana.geometry('600x400')
ventana.title('Manejo de grid')
ventana.iconbitmap('icono.ico')

# width cantidad de caracteres que entran en el input
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.DISABLED)
# entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, show='*')
entrada1 = ttk.Entry(ventana, width=30, justify=tk.CENTER, state=tk.NORMAL)
entrada1.grid(row=0, column=0)

# agregando texto al input
entrada1.insert(0, 'Introduce una cadena')
# entrada1.insert(5, '-')
# entrada1.insert(tk.END, '.')
# entrada1.config(state='readonly')


def enviar():
    print(entrada1.get())
    boton1.config(text=entrada1.get())
    # Eliminar el contendio del input
    # entrada1.delete(0, tk.END)
    # Seleccionar el texto del input
    entrada1.select_range(0, tk.END)
    # Para hacer efectivo la selección
    entrada1.focus()


# Creamos un botón para recoger los datos
boton1 = ttk.Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=0, column=1)

ventana.mainloop()