def add10(number):
    try:
        return number+10
    except TypeError:
        print("Error: Esto no es un numero")

# Ejemplo de división
resultado = add10('5')