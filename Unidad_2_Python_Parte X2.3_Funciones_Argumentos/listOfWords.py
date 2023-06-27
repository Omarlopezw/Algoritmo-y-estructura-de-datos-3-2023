words = []
number = int(input('Digite el numero de palabras: '))
i = 0

while(i != number):
    word = input('Palabra: ')
    while ' ' in word:
        word = input('Ingrese una sola palabra: ')
    else:
        words.append(word)
        i+=1


for word in words:
    print('%s, '%(word),end = '')

