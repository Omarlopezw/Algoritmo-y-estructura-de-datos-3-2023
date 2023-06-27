def dividir(dividendo, divisor):
    try:
        resultado = dividendo / divisor
        return resultado
    except ZeroDivisionError:
        print("Error: División entre cero no es válida")

# Ejemplo de división
resultado = dividir(27, 0)