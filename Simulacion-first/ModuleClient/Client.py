class Client:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.clientCode = ""

    def setName(self,name):
        self.name = name
    def setSurname(self,surname):
        self.surname = surname
    def setClientCode(self,clientCode):
        self.clientCode = clientCode
    def getName(self):
        return self.name
    def getSurname(self):
        return self.surname
    def getClientCode(self):
        return self.clientCode 
    