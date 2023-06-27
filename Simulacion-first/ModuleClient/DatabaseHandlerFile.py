import sqlite3
from tkinter import messagebox

class DatabaseHandler:

    def __init__(self):
        pass
    def connect(self):
        try:
            self.connection = sqlite3.connect("mydb.db")
            self.cursor = self.connection.cursor()

        except sqlite3.OperationalError:
                print('error load database: already created ')
        return self.connection
    
    def createTable(self,tableName,colums):
        self.sql = f"CREATE TABLE IF NOT EXISTS {tableName} ({', '.join(colums)})"
        try:
            self.connection.execute(self.sql)
            self.connection.commit()

            self.searchTable(tableName)
        except sqlite3.OperationalError:
                print(f'error: {tableName} already has created')

    def addClientRegister(self,name,surname,clientCode):
        try:
            ThreeEntryClientCode = str(clientCode[:3])  

            if ThreeEntryClientCode == '100':
                self.connection.execute("insert into Client(name,surname,clientCode) values (?,?,?)",(name,surname,clientCode))
                self.connection.commit()

                # Obtener el ID del último registro insertado
                ClientID = self.connection.execute("SELECT last_insert_rowid()").fetchone()[0]

                messagebox.showinfo("Success", f"Client has been added with ID: {ClientID}")
                print(f"client added with ID: {ClientID}")

                self.disconnect()
            else:
                messagebox.showerror("Error", "Invalid clientCode")


        except sqlite3.OperationalError:
            print(f'error:adding register failed ')


    def deleteClientRegister(self,clientCode):
            try:
                self.connection.execute(f"DELETE from Client where clientCode =?",(clientCode,))
                changedRow = self.connection.total_changes
                self.connection.commit()

                if changedRow == 0:
                    messagebox.showerror("Error", "error clientCode don't exits")
                else:
                    messagebox.showinfo("Success", "Client has been deleted")
                
                # self.connection.close()

            except sqlite3.Error as e:
                # Capturar la excepción si el registro no existe
                print("Error al eliminar el registro:", e)
    def updateClientRegister(self,columnName,columnValue,clientCode):
            try:
                self.connection.execute(f"UPDATE Client SET {columnName}=? where clientCode=?",(columnValue,clientCode,))
                self.connection.commit()

                messagebox.showinfo("Success", f"Client with clientCode {clientCode } has been updated in column -> {columnName} with value {columnValue}")
                print(f"register with clientCode {clientCode } IN Client updated in column{columnName} with value {columnValue}")
        
            except sqlite3.OperationalError:
                messagebox.showerror("Error", f'error:updating register failed')
                print(f'error:updating register failed ')

    def addColumnInTable(self, tableName, columnName, columnType):
        self.connection.execute(f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}")
        self.connection.commit()

        print(f"Column {columnName} added succesly in {tableName}")

    def searchClientRegister(self,clientCode):
            try:
                cursor = self.connection.execute(f"select * from Client where clientCode =?",(clientCode,))

                row = cursor.fetchone()

                if row != None:
                    messagebox.showinfo("Client", f"Client:\n{row}\n")
                    print(row)
                else:
                    messagebox.showerror("Error", "error with ID clientCode don't exits")

            except sqlite3.OperationalError:
                print(f'error:searching register failed ')
    def searchAllClients(self):

        # Realizar una consulta para obtener todos los registros de una tabla
        self.cursor.execute("SELECT * FROM Client")

        # Obtener todos los registros como una lista de tuplas
        clients = self.cursor.fetchall()

        # Imprimir los registros
        for client in clients:
            print(client)

        messagebox.showinfo("Client List", f"Client List:\n{clients}\n")

    def disconnect(self):
        self.connection.close()
        print('Disconnected...')

# db = DatabaseHandler()

# db.connect()

# Ejemplo de uso
# tableName = "Client"
# colums = ["id INTEGER PRIMARY KEY AUTOINCREMENT", "name TEXT","surname TEXT",
#             "clientCode TEXT"]

# # Crear la tabla utilizando los parámetros
# db.createTable(tableName,colums)

# db.searchTable('Client')

#Add register

# db.addClientRegister('Ramiro','Gomez','Chaco 5221')
# db.addTechnicianRegister('Mariano','Mano','24MUN521')
# db.addProblemRegister('Sin señal',1,2,'18-06-2023 3pm')
# db.addProblemRegister('Deco dañado',2,1,'18-06-2023 8am')

#Select in table

# db.searchRegister('Client',6)

#Delete in table

# db.deleteRegister('Client',3)

#adding column in table

# db.addColumnInTable('Problem','Date','TEXT')

#updating register 

# db.updateProblemRegister('Client','name','Manuel','1')

#Searching a register

# db.searchClientRegister('1')