from DatabaseHandlerFile import DatabaseHandler
from Client import Client
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class ClientHandler:

    def __init__(self):
        self.db = DatabaseHandler()
        self.db.connect()
    def addClient(self,name,surname):

        self.db.addClientRegister(name,surname)
    def deleteClient(self,clientCode):

        self.db.deleteClientRegister(clientCode)
        
    def searchClient(self,clientCode):

        self.db.searchClientRegister(clientCode)

    def updateClient(self,column,value,clientCode):
        self.db.updateClientRegister(column,value,clientCode)

    def searchAllClients(self):
        
        clientsData = self.db.searchAllClients()

        clients = []

        for clientData in clientsData:
            id, name, surname = clientData
            client = Client(id, name, surname)
            clients.append(client)
        return clients 
      
    # def prepareClientData(self):

    #     #prepare dataClient
    #     self.client.setName(self.viewReference.name.get())
    #     self.client.setSurname(self.viewReference.surname.get())

    #     #Use dataClient
    #     self.db.addClientRegister(self.client.getName(),self.client.getSurname())



# MngmtWind = ClientHandler()
# tk.mainloop()

