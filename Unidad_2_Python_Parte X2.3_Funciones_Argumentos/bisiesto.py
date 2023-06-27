year = int(input('Ingrese un año: '))

if(year%4 == 0 and (not(year%100 == 0))):
    print('%d es bisiesto'%(year))

elif(year%4 == 0 and year%400 == 0):
    print('%d es bisiesto'%(year))

else:
    print('%d no es bisiesto'%(year))
