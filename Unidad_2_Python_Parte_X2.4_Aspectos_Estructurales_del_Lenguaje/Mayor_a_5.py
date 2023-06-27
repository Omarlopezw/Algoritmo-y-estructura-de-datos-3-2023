listOfNumbers= [2,3,4,5,6,7]

def higherOfFive(number):
    return number > 5


HigherOfFive = list(filter(higherOfFive,listOfNumbers))

print('Numeros: ',listOfNumbers)
print('Mayores a 5: ',HigherOfFive)