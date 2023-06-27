dictionary = {}
option = int(input('¿Desea cargar un usuario? 1 para continuar o cualquier otro numero para finalizar: '))
while(option == 1):

    clave = input('ingrese el nombre de usuario: ')

    if clave in dictionary:
        print('Este usuario ya existe,intente con otro')
    
    else:

        valor = int(input('ingrese el numero de telefono: '))
        dictionary[clave] = valor
        
    option = int(input('¿Desea cargar otro usuario? 1 para continuar o cualquier otro numero para finalizar: '))


print(dictionary)