from DatabaseHandlerFile import DatabaseHandler
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ManagmentWindow(tk.Tk):

    def __init__(self):
        super(ManagmentWindow,self).__init__()
        self.title("Managment Window")
        self.db = DatabaseHandler()

        # Crear el widget Notebook
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Crear las subventanas dentro del Notebook
        # self.create_subwindow3()
        # self.create_subwindow1()
        # self.create_subwindow2()

        # self.mainloop()

    def create_subwindow1(self):
        self.subwindow1 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow1, text="Add Client")

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

        label3 = tk.Label(self.subwindow1,text='ClientCode')
        label3.grid(row=2, column=0, padx=5, pady=5)
        ClientCode = tk.Entry(self.subwindow1)
        ClientCode.grid(row=2, column=1, padx=5, pady=5)

        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow1,text = 'Send Data',
            command=lambda: self.db.addClientRegister(name.get(),surname.get(),ClientCode.get()) )
        button.grid(row=3,column=1)

    def create_subwindow2(self):
        self.subwindow2 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow2, text="Delete client")
        # Agregar contenido a la subventana 2
        self.subwindow2.config(width=300,height=300)

        label1 = tk.Label(self.subwindow2,text='ClientCode')
        label1.grid(row=0, column=0, padx=5, pady=5)
        ClientCode = tk.Entry(self.subwindow2)
        ClientCode.grid(row=0, column=1, padx=5, pady=5)

        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow2,text = 'Delete client',command=lambda: self.db.deleteClientRegister(ClientCode.get()) )
        button.grid(row=3,column=1)

    def create_subwindow3(self):

        self.subwindow3 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow3, text="Search Client")
        # Agregar contenido a la subventana 3
        self.subwindow3.config(width=300,height=300)

        label1 = tk.Label(self.subwindow3,text='codeClient')
        label1.grid(row=0, column=0, padx=5, pady=5)
        clientID = tk.Entry(self.subwindow3)
        clientID.grid(row=0, column=1, padx=5, pady=5)

        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow3,text = 'Search Client',command=lambda: self.db.searchClientRegister(int(clientID.get())))
        button.grid(row=4,column=1)
    def create_subwindow4(self):

        self.subwindow4 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow4, text="Update client")
        # Agregar contenido a la subventana 4
        self.subwindow4.config(width=400,height=400)

        label1 = tk.Label(self.subwindow4,text='Client code')
        label1.grid(row=0, column=0, padx=5, pady=5)
        clientCode = tk.Entry(self.subwindow4)
        clientCode.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow4,text='Column')
        label2.grid(row=1, column=0, padx=5, pady=5)
        Column = tk.Entry(self.subwindow4)
        Column.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow4,text='Value column')
        label3.grid(row=2, column=0, padx=5, pady=5)
        valueColumn = tk.Entry(self.subwindow4)
        valueColumn.grid(row=2, column=1, padx=5, pady=5)

        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow4,text = 'Update',
                        command=lambda: self.db.updateClientRegister(Column.get(),valueColumn.get(),clientCode.get()))
        button.grid(row=4,column=1)

    def create_subwindow5(self):

        self.subwindow5 = ttk.Frame(self.notebook)
        self.notebook.add(self.subwindow5, text="Search all Clients")
        # Agregar contenido a la subventana 5
        self.subwindow5.config(width=300,height=300)

        #Use DatabaseHandler
        self.db.connect()
        button = tk.Button(self.subwindow5,text = 'Search all clients',command=lambda: self.db.searchAllClients())
        button.grid(row=4,column=1)

# MngmtWind = ManagmentWindow()
# MngmtWind.create_subwindow1()

# tk.mainloop()