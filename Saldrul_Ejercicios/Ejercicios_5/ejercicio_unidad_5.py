from tkinter import *

root = Tk()
margen = Label(root, text="Ingrese sus datos")
margen.grid(row=0, column=5, sticky=N)
titulo = Label(root, text="Titulo")
titulo.grid(row=1, column=0, sticky=W)
ruta = Label(root, text="Ruta")
ruta.grid(row=2, column=0, sticky=W)
descripcion = Label(root, text="Descripción")
descripcion.grid(row=3, column=0, sticky=W)

entry_id = Entry(root)
entry_id.grid(row=1, column=5)
entry_nombre = Entry(root)
entry_nombre.grid(row=2, column=5)
entry_descripcion = Entry(root)
entry_descripcion.grid(row=3, column=5)


def funcion():
    print(entry_id, entry_descripcion, entry_nombre)


def funcion_a():
    root.text = "#C711F7"
    root.background = "#811BE0"
    root.foreground = "#1117ED"


boton_g = Button(root, text="Alta", command=funcion)
boton_g.grid(row=4, column=5)

boton_g = Button(root, text="Sorpresa", command=funcion_a)
boton_g.grid(row=4, column=8)

root.mainloop()
