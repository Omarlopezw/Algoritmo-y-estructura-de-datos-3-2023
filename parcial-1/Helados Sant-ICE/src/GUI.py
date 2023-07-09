from DessertOrderHandler import DessertOrderHandler
# from DessertOrder import DessertOrder
import tkinter as tk
from tkinter import ttk



class GUI(tk.Tk):

    def __init__(self):
        super(GUI,self).__init__()
        self.title("Managment Window")

        self.DessertOrderHandler = DessertOrderHandler()
        #Menu
        self.create_menu()

        #Create DessertOrder table
        self.createDessertOrderTable()

        #See all DessertOrders in a table
        self.refreshTable()

    def createSubwindow1(self):
        self.subwindow1 = tk.Toplevel(self)
        # Agregar contenido a la subventana 1
        self.subwindow1.config(width=300,height=300)
        label0 = tk.Label(self.subwindow1,text='Article code')
        label0.grid(row=0, column=0, padx=5, pady=5)
        self.aArticleCode = tk.Entry(self.subwindow1)
        self.aArticleCode.grid(row=0, column=1, padx=5, pady=5)

        label1 = tk.Label(self.subwindow1,text='Name')
        label1.grid(row=1, column=0, padx=5, pady=5)
        self.aName = tk.Entry(self.subwindow1)
        self.aName.grid(row=1, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow1,text='Surname')
        label2.grid(row=2, column=0, padx=5, pady=5)
        self.aSurname = tk.Entry(self.subwindow1)
        self.aSurname.grid(row=2, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow1,text='Address')
        label3.grid(row=3, column=0, padx=5, pady=5)
        self.aAddress = tk.Entry(self.subwindow1)
        self.aAddress.grid(row=3, column=1, padx=5, pady=5)

        label4 = tk.Label(self.subwindow1,text='Rate')
        label4.grid(row=4, column=0, padx=5, pady=5)
        self.aRate = tk.Entry(self.subwindow1)
        self.aRate.grid(row=4, column=1, padx=5, pady=5)

        self.buttonSW1 = tk.Button(self.subwindow1,text = 'Send Data',command=self.addDessertOrder )
        self.buttonSW1.grid(row=5,column=1)
    def createSubwindow2(self):
        self.subwindow2 = tk.Toplevel(self)

        # Agregar contenido a la subventana 2
        self.subwindow2.config(width=300,height=300)

        label1 = tk.Label(self.subwindow2,text='DessertOrderCode')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.dDessertOrderCode = tk.Entry(self.subwindow2)
        self.dDessertOrderCode.grid(row=0, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow2,text = 'Delete DessertOrder',command= self.deleteDessertOrder )
        button.grid(row=3,column=1)
    def createSubwindow3(self):
        self.subwindow3 = tk.Toplevel(self)
        # Agregar contenido a la subventana 3
        self.subwindow3.config(width=300,height=300)

        label1 = tk.Label(self.subwindow3,text='codeDessertOrder')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.sDessertOrderCode = tk.Entry(self.subwindow3)
        self.sDessertOrderCode.grid(row=0, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow3,text = 'Search DessertOrder',command=self.searchDessertOrder)
        button.grid(row=4,column=1)
    def createSubwindow4(self):
        
        self.subwindow4 = tk.Toplevel(self)
        # Agregar contenido a la subventana 4
        self.subwindow4.config(width=400,height=400)

        label1 = tk.Label(self.subwindow4,text='DessertOrder code')
        label1.grid(row=0, column=0, padx=5, pady=5)
        self.upDessertOrderCode = tk.Entry(self.subwindow4)
        self.upDessertOrderCode.grid(row=0, column=1, padx=5, pady=5)

        label2 = tk.Label(self.subwindow4,text='Column')
        label2.grid(row=1, column=0, padx=5, pady=5)
        self.upColumn = tk.Entry(self.subwindow4)
        self.upColumn.grid(row=1, column=1, padx=5, pady=5)

        label3 = tk.Label(self.subwindow4,text='Value column')
        label3.grid(row=2, column=0, padx=5, pady=5)
        self.upValueColumn = tk.Entry(self.subwindow4)
        self.upValueColumn.grid(row=2, column=1, padx=5, pady=5)

        button = tk.Button(self.subwindow4,text = 'Update',
                        command=self.updateDessertOrder)
        button.grid(row=4,column=1)

    def createSubwindow5(self):
        self.subwindow5 = tk.Toplevel(self)
        # Agregar contenido a la subventana 5
        self.subwindow5.config(width=300,height=300)

        button = tk.Button(self.subwindow5,text = 'Search all DessertOrders',command= self.DessertOrderHandler.searchAllDessertOrders)
        button.grid(row=4,column=1)

    def create_menu(self):
        self.menu_bar = tk.Menu(self)

        # Opciones del menú
        customers_menu = tk.Menu(self.menu_bar, tearoff=0)
        customers_menu.add_command(
            label="Add DessertOrder", command=self.createSubwindow1)
        customers_menu.add_command(
            label="Delete DessertOrder", command=self.createSubwindow2)
        customers_menu.add_command(
            label="Search DessertOrder", command=self.createSubwindow3)
        customers_menu.add_command(label="Update DessertOrder", 
        command=self.createSubwindow4)
        # customers_menu.add_command(
        #     label="See all DessertOrders", command=self.createSubwindow5)

        self.menu_bar.add_cascade(label="DessertOrders", menu=customers_menu)
        self.config(menu=self.menu_bar)

    # Método que crea la vista en tabla para listar todos los DessertOrderes.
    def createDessertOrderTable(self):
        self.table_frame = tk.Frame(self)
        self.table_frame.pack(padx=10, pady=10)

        self.table = ttk.Treeview(self.table_frame, columns=(
            "orderID","articleCode", "name", "surname","address","rate"))
        self.table.heading("orderID", text="Código del pedido")
        self.table.heading("articleCode", text="Código del articulo")
        self.table.heading("name", text="Nombre")
        self.table.heading("surname", text="Apellido")
        self.table.heading("address", text="Direccion")
        self.table.heading("rate", text="Precio")
        self.table.pack()

    # Función que refresca la tabla para mostrar los datos de los DessertOrderes guardados--- "*" desempaqueta para pasar en vez de toda la lista completa,los valores individualmente
    def refreshTable(self):
        self.table.delete(*self.table.get_children())
        DessertOrders = self.DessertOrderHandler.searchAllDessertOrders()

        # Calcula el índice de inserción deseado
        # insert_index = self.table.size // 2
        if DessertOrders:
            for DessertOrder in DessertOrders:
                self.table.insert("", "end", values=(
                    DessertOrder.orderID,DessertOrder.articleCode, DessertOrder.name, DessertOrder.surname,DessertOrder.address,DessertOrder.rate))
        else:
            self.table.insert("", "end", values=(
                "No hay ordenes de postres cargados.", "", "", ""))
    def addDessertOrder(self):
        self.DessertOrderHandler.addDessertOrder(self.aArticleCode.get(),self.aName.get(),self.aSurname.get(),self.aAddress.get(),self.aRate.get())
        self.subwindow1.destroy()
        self.refreshTable()
    
    def deleteDessertOrder(self):
        self.DessertOrderHandler.deleteDessertOrder(self.dDessertOrderCode.get())
        self.subwindow2.destroy()
        self.refreshTable()

    def searchDessertOrder(self):
        self.DessertOrderHandler.searchDessertOrder(int(self.sDessertOrderCode.get()))

    def updateDessertOrder(self):
        self.DessertOrderHandler.updateDessertOrder(self.upColumn.get(),self.upValueColumn.get(),self.upDessertOrderCode.get())
        self.subwindow4.destroy()
        self.refreshTable()

    def exit_program(self):
        self.destroy()

    def run(self):
        self.mainloop()

# Crear una instancia de la clase GUI y ejecutar la aplicación
app = GUI()
app.run()
