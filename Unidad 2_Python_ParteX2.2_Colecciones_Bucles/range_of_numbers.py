number1 = int(input('Ingrese un numero: '))
number2 = int(input('Ingrese otro numero: '))

if(number1 < number2):
    i = number1+1
    while(i < number2):
        print(i,)
        i+=1
else:
    i = number2+1
    while(i < number1):
        print(i,)
        i+=1
