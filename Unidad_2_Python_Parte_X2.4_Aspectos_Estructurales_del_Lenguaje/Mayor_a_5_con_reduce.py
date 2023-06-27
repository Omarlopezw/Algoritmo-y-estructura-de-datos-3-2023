from functools import reduce

listOfNumbers= [2,3,4,5,6,7]

def higherOfFive(count,number):
    if number > 5:
        return count + 1
    else:
        return  count



HigherOfFive = reduce(higherOfFive,listOfNumbers,0)

print('Numeros: ',listOfNumbers)
print('Mayores a 5: ',HigherOfFive)