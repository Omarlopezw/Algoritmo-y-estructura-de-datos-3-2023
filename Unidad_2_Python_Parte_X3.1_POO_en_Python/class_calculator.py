class Calculator:
    version = '1.0'
    def __init__(self,acumulator):
        self.acumulator = acumulator
    def add(self,*args):
        for arg in args:
            self.acumulator +=arg
        return self.acumulator
    def subs(self,*args):
        for arg in args:
            self.acumulator -=arg
        return self.acumulator
    def multiplication(self,*args):
        for arg in args:
            self.acumulator *=arg
        return self.acumulator
    def divition(self,*args):
        for arg in args:
            self.acumulator /=arg
        return self.acumulator
    @classmethod
    def getVersion(cls):
        return cls.version
    @staticmethod
    def turnON():
        print('Encendiendo.........')
    @staticmethod
    def turnOFF():
        print('Apagando.........')
        

    
acumulator = 0
calculadora = Calculator(acumulator)
print(Calculator.turnON())
print(calculadora.add(2+2+2+2+2))
print(Calculator.version)
print(Calculator.getVersion())
print(Calculator.turnOFF())