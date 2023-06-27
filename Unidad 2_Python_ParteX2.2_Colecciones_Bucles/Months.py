months = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

userNumber = int(input('Ingrese un numero: '))

if userNumber in range(1,(len(months))+1):
    print('Representa el mes: %s '%(months[userNumber-1]))

else:
    print('ERROR')