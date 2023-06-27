from DatabaseHandlerFile import DatabaseHandler
import tkinter as tk
from tkinter import ttk

    


class ManagmentWindow(tk.Tk):

    def __init__(self):
        super(ManagmentWindow,self).__init__()
        self.title("Managment Window")
        self.db = DatabaseHandler()

        # Crear el widget Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear las subventanas dentro del Notebook
        self.create_subwindow3()
        self.create_subwindow1()
        self.create_subwindow2()

        self.mainloop()

    def create_subwindow1(self):
        self.subwindow1 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow1, text="Client")

        # Agregar contenido a la subventana 1
        self.subwindow1.config(width=300,height=300)
        label1 = tk.Label(self.subwindow1,text='Name')
        label1.grid(row=0, column=0, padx=5, pady=5)
        name = tk.Entry(self.subwindow1)
        name.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow1,text='Surname')
        label2.grid(row=1, column=0, padx=5, pady=5)
        surname = tk.Entry(self.subwindow1)
        surname.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow1,text='Address')
        label3.grid(row=2, column=0, padx=5, pady=5)
        address = tk.Entry(self.subwindow1)
        address.grid(row=2, column=1, padx=5, pady=5)

        #Use DatabaseHandler
        self.db.connect()

        button = tk.Button(self.subwindow1,text = 'Send Data',
                            command=lambda: self.db.addClientRegister(name.get(),surname.get(),address.get()) )
        button.grid(row=3,column=1)

    def create_subwindow2(self):
        self.subwindow2 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow2, text="Technician")
        # Agregar contenido a la subventana 2
        self.subwindow2.config(width=300,height=300)

        label1 = tk.Label(self.subwindow2,text='Name')
        label1.grid(row=0, column=0, padx=5, pady=5)
        name = tk.Entry(self.subwindow2)
        name.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow2,text='Surname')
        label2.grid(row=1, column=0, padx=5, pady=5)
        surname = tk.Entry(self.subwindow2)
        surname.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow2,text='Movil')
        label3.grid(row=2, column=0, padx=5, pady=5)
        movil = tk.Entry(self.subwindow2)
        movil.grid(row=2, column=1, padx=5, pady=5)

        #Use DatabaseHandler

        self.db.connect()
        button = tk.Button(self.subwindow2,text = 'Send Data',
                            command=lambda: self.db.addTechnicianRegister(name.get(),surname.get(),movil.get()) )
        button.grid(row=3,column=1)

    def create_subwindow3(self):

        self.subwindow3 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow3, text="Problem")
        # Agregar contenido a la subventana 3
        self.subwindow3.config(width=300,height=300)

        label1 = tk.Label(self.subwindow3,text='Name')
        label1.grid(row=0, column=0, padx=5, pady=5)
        name = tk.Entry(self.subwindow3)
        name.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow3,text='ClientID')
        label2.grid(row=1, column=0, padx=5, pady=5)
        clientID = tk.Entry(self.subwindow3)
        clientID.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow3,text='Technician')
        label3.grid(row=2, column=0, padx=5, pady=5)
        technicianID = tk.Entry(self.subwindow3)
        technicianID.grid(row=2, column=1, padx=5, pady=5)

        label4 = tk.Label(self.subwindow3,text='Date')
        label4.grid(row=3, column=0, padx=5, pady=5)
        date = tk.Entry(self.subwindow3)
        date.grid(row=3, column=1, padx=5, pady=5)


        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow3,text = 'Send Data',
                            command=lambda: self.db.addProblemRegister(name.get(),clientID.get(),technicianID.get(),date.get()) )
        button.grid(row=4,column=1)

# MngmtWind = ManagmentWindow()