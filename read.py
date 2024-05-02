# Abrir el archivo en modo lectura
with open('archivo.txt', 'r') as archivo:
    # Leer cada línea del archivo e imprimirla
    for linea in archivo:
        print(linea.strip())  # strip() para eliminar caracteres de nueva línea
