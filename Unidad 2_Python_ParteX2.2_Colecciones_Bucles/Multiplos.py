userNumber = int(input('Ingrese un numero: '))
listOfNumbers = []

for number in range(1,11):
    listOfNumbers.append(userNumber*number)

for number in listOfNumbers:
    print(number)

