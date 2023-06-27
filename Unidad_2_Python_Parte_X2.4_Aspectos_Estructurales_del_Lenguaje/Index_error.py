listOfNumbers = [1,2,3,4,5,6]
number = 8
i = 0
while(i <= number):
    try:
        print(listOfNumbers[i])
        i+=1
    except IndexError:
        print("Error: Indice del array excedido")
        break

# lista = [1, 2, 3]

# try:
#     for i in range(len(lista)+5):
#         print(lista[i])
# except IndexError:
#     print("Error: Índice fuera de rango")
