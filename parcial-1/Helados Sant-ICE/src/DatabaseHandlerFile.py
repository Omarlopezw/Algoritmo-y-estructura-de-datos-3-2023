import sqlite3
from tkinter import messagebox

class DatabaseHandler:

    def __init__(self):
        pass
    def connect(self):
        try:
            self.connection = sqlite3.connect("DessertOrder.db")
            self.cursor = self.connection.cursor()

        except sqlite3.OperationalError:
                print('error load database: already created ')
        return self.connection
    
    def createTable(self,tableName,colums):
        self.sql = f"CREATE TABLE IF NOT EXISTS {tableName} ({', '.join(colums)})"
        try:
            self.connection.execute(self.sql)
            self.connection.commit()
                    
            # Solo va a insertar el valor 99 de id atoincremental
            # para empezar cn código en valor igual a 100 si no 
            # existe la columna name con el valor 'customers',
            # esto significa que solo se insertará la primera
            # vez que se crea la tabla customers.
            self.cursor.execute("""
                INSERT INTO sqlite_sequence (name, seq)
                SELECT 'DessertOrder', 99
                WHERE NOT EXISTS (SELECT 1 FROM sqlite_sequence WHERE name = 'DessertOrder')
            """)   
            self.connection.commit()
            # self.searchTable(tableName)
        except sqlite3.OperationalError:
                print(f'error: {tableName} already has been created')

    def addDessertOrderRegister(self,articleCode,clientName,clientSurname,clientAddress,rate):
        try:
            # ThreeEntryDessertOrderCode = str(DessertOrderCode[:3])  

            # if ThreeEntryDessertOrderCode == '100':
                self.connection.execute("insert into DessertOrder(articleCode,name,surname,address,rate) values (?,?,?,?,?)",
                                        (articleCode,clientName,clientSurname,clientAddress,rate))
                self.connection.commit()

                # Obtener el ID del último registro insertado
                DessertOrderID = self.connection.execute("SELECT last_insert_rowid()").fetchone()[0]

                messagebox.showinfo("Success", f"DessertOrder has been added with ID: {DessertOrderID}")
                print(f"DessertOrder added with ID: {DessertOrderID}")
            # else:
            #     messagebox.showerror("Error", "Invalid DessertOrderCode")

        except sqlite3.OperationalError:
            print(f'error:adding register failed ')


    def deleteDessertOrderRegister(self,id):
            try:
                self.connection.execute(f"DELETE from DessertOrder where id =?",(id,))
                changedRow = self.connection.total_changes
                self.connection.commit()

                if changedRow == 0:
                    messagebox.showerror("Error", "error DessertOrderCode don't exits")
                else:
                    messagebox.showinfo("Success", "DessertOrder has been deleted")
                
                # self.connection.close()

            except sqlite3.Error as e:
                # Capturar la excepción si el registro no existe
                print("Error al eliminar el registro:", e)
    def updateDessertOrderRegister(self,columnName,columnValue,DessertOrderCode):
            try:
                self.connection.execute(f"UPDATE DessertOrder SET {columnName}=? where id=?",(columnValue,DessertOrderCode,))
                self.connection.commit()

                messagebox.showinfo("Success", f"DessertOrder with DessertOrderCode {DessertOrderCode } has been updated in column -> {columnName} with value {columnValue}")
                print(f"register with DessertOrderCode {DessertOrderCode } IN DessertOrder updated in column{columnName} with value {columnValue}")
        
            except sqlite3.OperationalError:
                messagebox.showerror("Error", f'error:updating register failed')
                print(f'error:updating register failed ')

    def addColumnInTable(self, tableName, columnName, columnType):
        self.connection.execute(f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}")
        self.connection.commit()

        print(f"Column {columnName} added succesly in {tableName}")

    def searchDessertOrderRegister(self,DessertOrderCode):
            try:
                cursor = self.connection.execute(f"select * from DessertOrder where id =?",(DessertOrderCode,))

                row = cursor.fetchone()

                if row != None:
                    messagebox.showinfo("DessertOrder", f"DessertOrder:\n{row}\n")
                    print(row)
                else:
                    messagebox.showerror("Error", "error with ID DessertOrderCode don't exits")

            except sqlite3.OperationalError:
                print(f'error:searching register failed ')
    def searchAllDessertOrders(self):

        # Realizar una consulta para obtener todos los registros de una tabla
        self.cursor.execute("SELECT * FROM DessertOrder")

        # Obtener todos los registros como una lista de tuplas
        DessertOrders = self.cursor.fetchall()

        # Imprimir los registros
        for DessertOrder in DessertOrders:
            print(DessertOrder)
        return DessertOrders 

    def disconnect(self):
        self.connection.close()
        print('Disconnected...')

# db = DatabaseHandler()

# db.connect()

# # Ejemplo de uso
# tableName = "DessertOrder"
# colums = ["id INTEGER PRIMARY KEY AUTOINCREMENT ", "articleCode INTEGER","name TEXT","surname TEXT","address TEXT","rate REAL"]

# # # Crear la tabla utilizando los parámetros
# db.createTable(tableName,colums)

# db.searchTable('DessertOrder')

#Add register

# db.addDessertOrderRegister('Ramiro','Gomez','Chaco 5221')
# db.addTechnicianRegister('Mariano','Mano','24MUN521')
# db.addProblemRegister('Sin señal',1,2,'18-06-2023 3pm')
# db.addProblemRegister('Deco dañado',2,1,'18-06-2023 8am')

#Select in table

# db.searchRegister('DessertOrder',6)

#Delete in table

# db.deleteRegister('DessertOrder',3)

#adding column in table

# db.addColumnInTable('Problem','Date','TEXT')

#updating register 

# db.updateProblemRegister('DessertOrder','name','Manuel','1')

#Searching a register

# db.searchDessertOrderRegister('1')