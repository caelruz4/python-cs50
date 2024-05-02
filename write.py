# Abrir el archivo en modo escritura
with open('archivo.txt', 'w') as archivo:
    # Lista de cadenas
    lineas = ["Hola mundo\n", "Esto es una prueba\n", "Bye bye\n"]
    
    # Escribir cada cadena en una línea del archivo
    archivo.writelines(lineas)
