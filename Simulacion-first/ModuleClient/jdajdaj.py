from Client import Client
import tkinter as tk
from tkinter import ttk

class test(tk.Tk):
        def __init__(self) -> None:
            super(test,self).__init__()
            self.title("Managment Window")

            # Crear el widget Notebook
            self.notebook = ttk.Notebook(self)
            self.notebook.pack(fill=tk.BOTH, expand=True)
            self.client = Client()  
            self.addClient() 
            self.mainloop()
        def getname(self):
            self.setName(self.name.get())

            print(self.client.getName())
            return self.client.getName()
        def setName(self,name):
            return self.client.setName(name)
        def addClient(self):

            #Se podria mover toda la ventana
            self.subwindow1 = ttk.Frame(self.notebook)
            self.notebook.add(self.subwindow1, text="Add Client")

            # Agregar contenido a la subventana 1
            self.subwindow1.config(width=300,height=300)
            label1 = tk.Label(self.subwindow1,text='Name')
            label1.grid(row=0, column=0, padx=5, pady=5)
            self.name = tk.Entry(self.subwindow1)
            self.name.grid(row=0, column=1, padx=5, pady=5)
            button = tk.Button(self.subwindow1,text = 'Send Data',command=self.getname) 
            button.grid(row=3,column=1)
            self.getname()
        def tests(self):
             pass


tesst = test()
print(tesst.getname())
# tk.mainloop()self.mainloop()self.mainloop()