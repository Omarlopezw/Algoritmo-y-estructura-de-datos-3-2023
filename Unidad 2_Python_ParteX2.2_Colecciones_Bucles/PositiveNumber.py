number = int(input('Ingrese un numero positivo: '))

while(number < 0):
    print('Este numero no es impar: %d'%(number))
    number = int(input('Ingrese nuevamente un numero positivo: '))