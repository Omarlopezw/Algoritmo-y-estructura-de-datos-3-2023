archivo = open("miarchivo.txt", "r")

# Obtener el estado del archivo
estado = archivo.read()

# Obtener el modo de apertura del archivo
modo_apertura = archivo.mode

# Obtener el nombre del archivo
nombre_archivo = archivo.name

# Obtener la codificación de caracteres del archivo
codificacion = archivo.encoding

# Cerrar el archivo
archivo.close()

# Mostrar la información obtenida
print("Contenido del archivo:")
print(estado)
print("Modo de apertura:", modo_apertura)
print("Nombre del archivo:", nombre_archivo)
print("Codificación de caracteres:", codificacion)
