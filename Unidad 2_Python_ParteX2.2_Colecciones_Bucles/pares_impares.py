listNumber = []

while(len(listNumber) != 2):
    number = int(input('Ingrese un numero: '))

    listNumber.append(number)

for number in listNumber:
    if(number%2 == 0):
        print('Este numero es par: %d'%(number))
    else:
        print('Este numero es impar: %d'%(number))