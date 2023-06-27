dictionary = {'juan': 12,'pedro' : 10}
searchKey = 'Omar'
# searchKey = 'juan'

try:
    print(dictionary[searchKey])
except KeyError:
    print("Error: Clave Inexistente")

