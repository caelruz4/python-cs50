import csv
import pandas as pd

def contar_votos(archivo_csv):
    recuento_votos = {}
    with open(archivo_csv, 'r') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            opcion = fila['opcion']
            if opcion in recuento_votos:
                recuento_votos[opcion] += 1
            else:
                recuento_votos[opcion] = 1
    return recuento_votos

def encontrar_ganador(recuento_votos):
    max_votos = 0
    ganador = []
    for opcion, votos in recuento_votos.items():
        if votos > max_votos:
            max_votos = votos
            # Una lista que contiene un solo elemento, es decir, se reinicia la lista
            ganador = [opcion]

        elif votos == max_votos:
            ganador.append(opcion)
    return ganador


archivo_csv = 'encuesta.csv'
resultado = contar_votos(archivo_csv)

# Convertir el diccionario de resultados en un DataFrame de Pandas
df = pd.DataFrame.from_dict(resultado, orient='index', columns=['Votos'])
df = df.sort_values(by='Votos', ascending=False)

# Imprimir el DataFrame
print("Resultados:")
print(df)

# Encontrar y mostrar el ganador
ganador = encontrar_ganador(resultado)
print(f'\nEl ganador es: {ganador[0]}')
