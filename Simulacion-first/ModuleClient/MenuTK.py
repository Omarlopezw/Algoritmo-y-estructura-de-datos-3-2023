from ClientHandler import ClientHandler
import tkinter as tk


class MenuApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('200x200')
        self.root.title("Menú")

        self.create_menu()

    def create_menu(self):
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        button1 = tk.Button(self.root,text = 'Add client', command=self.addClient, bd=6)
        button1.grid(row=3,column=1,padx=5, pady=5)
        button2 = tk.Button(self.root,text = 'Delete client by clientCode', command=self.deleteClient,bd=6)
        button2.grid(row=4,column=1,padx=5, pady=5)
        button3 = tk.Button(self.root,text = 'Update client', command=self.updateClient,bd=6)
        button3.grid(row=6,column=1,padx=5, pady=5)
        button4 = tk.Button(self.root,text = 'Read all clients', command=self.readAllClients,bd=6)
        button4.grid(row=7,column=1,padx=5, pady=5)
        button5 = tk.Button(self.root,text = 'Read client', command=self.readClient,bd=6)
        button5.grid(row=8,column=1,padx=5, pady=5)


    def addClient(self):
        self.root.destroy()
        self.ClientHandler = ClientHandler()
        self.ClientHandler.addClient()
    def deleteClient(self):
        self.root.destroy()
        self.ClientHandler = ClientHandler()
        self.ClientHandler.deleteClient()

    def updateClient(self):
        self.root.destroy()
        self.ClientHandler = ClientHandler()
        self.ClientHandler.updateClient()
    def readAllClients(self):
        self.root.destroy()
        self.ClientHandler = ClientHandler()
        self.ClientHandler.searchAllClients()
    def readClient(self):
        self.root.destroy()
        self.ClientHandler = ClientHandler()
        self.ClientHandler.searchClient()

    def exit_program(self):
        self.root.destroy()

    def run(self):
        self.root.mainloop()

# Crear una instancia de la clase MenuApp y ejecutar la aplicación
app = MenuApp()
app.run()
