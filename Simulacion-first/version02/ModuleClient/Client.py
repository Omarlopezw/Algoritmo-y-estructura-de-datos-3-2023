class Client:
    def __init__(self,clientCode,name,surname):
        self.clientCode = clientCode
        self.name = name
        self.surname = surname

    def setName(self,name):
        self.name = name
    def setSurname(self,surname):
        self.surname = surname
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
 
    