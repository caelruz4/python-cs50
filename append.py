# Datos a agregar al archivo
nuevo_contenido = "Este es un nuevo contenido que sera agregado al archivo."

# Abrir el archivo en modo append ('a')
archivo = open('archivo.txt', 'a')

# Agregar el nuevo contenido al final del archivo
archivo.write(nuevo_contenido + '\n')

# Cerrar el archivo después de usarlo
archivo.close()

print("Contenido agregado exitosamente al archivo.")
