class Animal:
    def __init__(self,name,edad):
        self.name = name
        self.edad = edad
    def eat(self):
        print('Estoy comiendo')

class Cat(Animal):
    especie = 'mamífero'
    peso = 40
    def __init__(self, name, edad,nickname,peso):
        super().__init__(name, edad)
        self.nickname = nickname
        self.peso = peso
    def arañar(self):
        print('Estoy arañando')
    @classmethod #Metoodo de Clase
    def get_peso_promedio(cls):
        return cls.peso
    @staticmethod
    def play():
        phrase = 'Estoy juando estaticamente'
        return phrase

myCat = Cat('gato',4,'reina',15)

print(myCat.nickname)
print(myCat.peso)
print(Cat.especie)
print(Cat.get_peso_promedio())
print(Cat.play())
