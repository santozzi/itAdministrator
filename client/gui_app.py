import tkinter as tk

def barra_menu(root):
    barra_menu = tk.Menu(root)
    root.config(menu=barra_menu,width=300, height =300)
    menu_inicio = tk.Menu(barra_menu, tearoff=0)
    barra_menu.add_cascade(label="inicio", menu=menu_inicio)
    menu_inicio.add_command(label="Crear Registro en DB")
    menu_inicio.add_command(label="Eliminargistro en DB")
    menu_inicio.add_command(label="Salir", command= root.destroy)



class Frame(tk.Frame):
    def __init__(self,root=None):
        super().__init__(root)
        self.root =root
        self.pack()
        self.config(width=500, height=350)
        self.config(bg="red")