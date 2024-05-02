import json

# Abrir el archivo JSON en modo lectura
with open('datos.json', 'r') as archivo:
    # Cargar los datos desde el archivo JSON a un diccionario
    datos = json.load(archivo)
    # Imprimir el diccionario cargado
    print(datos)
