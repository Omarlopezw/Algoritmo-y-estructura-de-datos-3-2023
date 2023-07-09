from DatabaseHandlerFile import DatabaseHandler
from DessertOrder import DessertOrderr
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class DessertOrderHandler:

    def __init__(self):
        self.db = DatabaseHandler()
        self.db.connect()
    def addDessertOrder(self,articleCode,name,surname,address,rate):

        self.db.addDessertOrderRegister(articleCode,name,surname,address,rate)
    def deleteDessertOrder(self,DessertOrderCode):

        self.db.deleteDessertOrderRegister(DessertOrderCode)
        
    def searchDessertOrder(self,DessertOrderCode):

        self.db.searchDessertOrderRegister(DessertOrderCode)

    def updateDessertOrder(self,column,value,DessertOrderCode):
        self.db.updateDessertOrderRegister(column,value,DessertOrderCode)

    def searchAllDessertOrders(self):
        
        DessertOrdersData = self.db.searchAllDessertOrders()

        DessertOrders = []

        for DessertOrderData in DessertOrdersData:
            id,articleCode, name, surname ,address,amount = DessertOrderData
            DessertOrder = DessertOrderr(id,articleCode, name, surname,address,amount)
            DessertOrders.append(DessertOrder)
        return DessertOrders 
    # def prepareDessertOrderData(self):

    #     #prepare dataDessertOrder
    #     self.DessertOrder.setName(self.viewReference.name.get())
    #     self.DessertOrder.setSurname(self.viewReference.surname.get())

    #     #Use dataDessertOrder
    #     self.db.addDessertOrderRegister(self.DessertOrder.getName(),self.DessertOrder.getSurname())



# MngmtWind = DessertOrderHandler()
# tk.mainloop()

