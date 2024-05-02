import json
datos = {"nombre": "Juan", "edad": 30, "ciudad": "Madrid"}
with open('datos.json', 'w') as archivo:
    # Escribir el diccionario en formato JSON en el archivo
    json.dump(datos, archivo)
