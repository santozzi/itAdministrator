import tkinter as tk
from client.gui_app import *
def main():
    root=tk.Tk()
    app = Frame(root=root)
    
    barra_menu(root)
    app.campos_peliculas()
    root.mainloop()
if __name__ == '__main__':
    main()