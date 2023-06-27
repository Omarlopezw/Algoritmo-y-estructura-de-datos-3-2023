import sqlite3

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

    def addClientRegister(self,name,surname,address):
        try:
            self.connection.execute("insert into Client(name,surname,address) values (?,?,?)",(name,surname,address))
            self.connection.commit()

            # Obtener el ID del último registro insertado
            ClientID = self.connection.execute("SELECT last_insert_rowid()").fetchone()[0]

            print(f"client added with ID: {ClientID}")

            self.disconnect()

        except sqlite3.OperationalError:
            print(f'error:adding register failed ')

    def addTechnicianRegister(self,name,surname,movil):
            try:
                self.connection.execute("insert into Technician(name,surname,movil) values (?,?,?)",(name,surname,movil))
                self.connection.commit()

                # Obtener el ID del último registro insertado
                TechnicianID = self.connection.execute("SELECT last_insert_rowid()").fetchone()[0]

                print(f"Technician added with ID: {TechnicianID}")
                self.disconnect()
            except sqlite3.OperationalError:
                print(f'error:adding register failed ')


    def addProblemRegister(self,name,CLientID,TechnicianID,Date):
            try:
                self.connection.execute("insert into Problem(name,Client_id,Technician_id,Date) values (?,?,?,?)",(name,CLientID,TechnicianID,Date))
                self.connection.commit()

                # Obtener el ID del último registro insertado
                ProblemID = self.connection.execute("SELECT last_insert_rowid()").fetchone()[0]

                print(f"Problem added with ID: {ProblemID}")
                self.disconnect()

            except sqlite3.OperationalError:
                print(f'error:adding register failed ')
    def searchRegister(self,tableName,ID):
            try:
                cursor = self.connection.execute(f"select * from {tableName} where id =?",(ID,))

                row = cursor.fetchone()

                if row != None:
                    print(row)
                else:
                    print(f"error with ID {ID} don't exits")

            except sqlite3.OperationalError:
                print(f'error:searching register failed ')

    def deleteRegister(self,tableName,ID):
            try:
                self.connection.execute(f"DELETE from {tableName} where id =?",(ID,))
                self.connection.commit()

                print(f'Register {ID} deleted in {tableName}')
                self.connection.close()

            except sqlite3.OperationalError:
                print(f'error:deleting register failed ')
    def updateProblemRegister(self,tableName,columnName,columnValue,ID):
            try:
                self.connection.execute(f"UPDATE {tableName} SET {columnName}=? where id=?",(columnValue,ID,))
                self.connection.commit()

                print(f"register {ID } IN {tableName} updated in column{columnName} with value {columnValue}")
        
            except sqlite3.OperationalError:
                print(f'error:updating register failed ')

    def addColumnInTable(self, tableName, columnName, columnType):
        self.connection.execute(f"ALTER TABLE {tableName} ADD COLUMN {columnName} {columnType}")
        self.connection.commit()

        print(f"Column {columnName} added succesly in {tableName}")

    def searchTable(self,tableName):
        # Conectarse a la base de datos
        cursor = self.connection.cursor()

        # Consultar la lista de objetos en la base de datos
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = cursor.fetchall()

        # Verificar si el nombre de la tabla está en la lista
        if (tableName,) in tables:
            print(f"La tabla '{tableName}' está creada.")
        else:
            print(f"La tabla '{tableName}' no está creada.")

    def disconnect(self):
        self.connection.close()
        print('Disconnected...')

# db = DatabaseHandler()

# db.connect()

# Ejemplo de uso
# tableName = "Problem"
# colums = ["id INTEGER PRIMARY KEY AUTOINCREMENT", "name TEXT","Client_id INTEGER",
#             "Technician_id INTEGER",
#             "FOREIGN KEY (Client_id) REFERENCES Client(id)"
#             ,"FOREIGN KEY (Technician_id) REFERENCES Technician(id)"]

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