from ClientHandler import ClientHandler
from Client import Client
import tkinter as tk
from tkinter import ttk



class GUI(tk.Tk):

    def __init__(self):
        super(GUI,self).__init__()
        self.title("Managment Window")

        self.clientHandler = ClientHandler()
        #Menu
        self.create_menu()

        #Create client table
        self.createClientTable()

        #See all clients in a table
        self.refreshTable()

    def createSubwindow1(self):
        self.subwindow1 = tk.Toplevel(self)
        # Agregar contenido a la subventana 1
        self.subwindow1.config(width=300,height=300)
        label1 = tk.Label(self.subwindow1,text='Name')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.aName = tk.Entry(self.subwindow1)
        self.aName.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow1,text='Surname')
        label2.grid(row=1, column=0, padx=5, pady=5)
        self.aSurname = tk.Entry(self.subwindow1)
        self.aSurname.grid(row=1, column=1, padx=5, pady=5)

        self.buttonSW1 = tk.Button(self.subwindow1,text = 'Send Data',command=self.addClient )
        self.buttonSW1.grid(row=3,column=1)
    def createSubwindow2(self):
        self.subwindow2 = tk.Toplevel(self)

        # Agregar contenido a la subventana 2
        self.subwindow2.config(width=300,height=300)

        label1 = tk.Label(self.subwindow2,text='ClientCode')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.dClientCode = tk.Entry(self.subwindow2)
        self.dClientCode.grid(row=0, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow2,text = 'Delete client',command= self.deleteClient )
        button.grid(row=3,column=1)
    def createSubwindow3(self):
        self.subwindow3 = tk.Toplevel(self)
        # Agregar contenido a la subventana 3
        self.subwindow3.config(width=300,height=300)

        label1 = tk.Label(self.subwindow3,text='codeClient')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.sClientCode = tk.Entry(self.subwindow3)
        self.sClientCode.grid(row=0, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow3,text = 'Search Client',command=self.searchClient)
        button.grid(row=4,column=1)
    def createSubwindow4(self):
        
        self.subwindow4 = tk.Toplevel(self)
        # Agregar contenido a la subventana 4
        self.subwindow4.config(width=400,height=400)

        label1 = tk.Label(self.subwindow4,text='Client code')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.upClientCode = tk.Entry(self.subwindow4)
        self.upClientCode.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow4,text='Column')
        label2.grid(row=1, column=0, padx=5, pady=5)
        self.upColumn = tk.Entry(self.subwindow4)
        self.upColumn.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow4,text='Value column')
        label3.grid(row=2, column=0, padx=5, pady=5)
        self.upValueColumn = tk.Entry(self.subwindow4)
        self.upValueColumn.grid(row=2, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow4,text = 'Update',
                        command=self.updateClient)
        button.grid(row=4,column=1)

    def createSubwindow5(self):
        self.subwindow5 = tk.Toplevel(self)
        # Agregar contenido a la subventana 5
        self.subwindow5.config(width=300,height=300)

        button = tk.Button(self.subwindow5,text = 'Search all clients',command= self.clientHandler.searchAllClients)
        button.grid(row=4,column=1)

    def create_menu(self):
        self.menu_bar = tk.Menu(self)

        # Opciones del menú
        customers_menu = tk.Menu(self.menu_bar, tearoff=0)
        customers_menu.add_command(
            label="Add client", command=self.createSubwindow1)
        customers_menu.add_command(
            label="Delete client", command=self.createSubwindow2)
        customers_menu.add_command(
            label="Search client", command=self.createSubwindow3)
        customers_menu.add_command(label="Update client", 
        command=self.createSubwindow4)
        # customers_menu.add_command(
        #     label="See all clients", command=self.createSubwindow5)

        self.menu_bar.add_cascade(label="Clients", menu=customers_menu)
        self.config(menu=self.menu_bar)

    # Método que crea la vista en tabla para listar todos los clientes.
    def createClientTable(self):
        self.table_frame = tk.Frame(self)
        self.table_frame.pack(padx=10, pady=10)

        self.table = ttk.Treeview(self.table_frame, columns=(
            "clientCode", "name", "surname"))
        self.table.heading("clientCode", text="Código")
        self.table.heading("name", text="Nombre")
        self.table.heading("surname", text="Apellido")
        self.table.pack()

     # Método que refresca la tabla para mostrar los datos de los clientes guardados
    def refreshTable(self):
        self.table.delete(*self.table.get_children())
        clients = self.clientHandler.searchAllClients()
        if clients:
            for client in clients:
                self.table.insert("", "end", values=(
                    client.clientCode, client.name, client.surname))
        else:
            self.table.insert("", "end", values=(
                "No hay clientes cargados.", "", "", ""))
    def addClient(self):
        self.clientHandler.addClient(self.aName.get(),self.aSurname.get())
        self.subwindow1.destroy()
        self.refreshTable()
    
    def deleteClient(self):
        self.clientHandler.deleteClient(self.dClientCode.get())
        self.subwindow2.destroy()
        self.refreshTable()

    def searchClient(self):
        self.clientHandler.searchClient(int(self.sClientCode.get()))

    def updateClient(self):
        self.clientHandler.updateClient(self.upColumn.get(),self.upValueColumn.get(),self.upClientCode.get())
        self.subwindow4.destroy()
        self.refreshTable()

    def exit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()

# Crear una instancia de la clase GUI y ejecutar la aplicación
app = GUI()
app.run()
