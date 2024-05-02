import os

def crear_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'w') as f:
            f.write('¡Hola, mundo!\n')
        print("Archivo " + nombre_archivo + " creado exitosamente.")
    except IOError:
        print("Error: no se pudo crear el archivo " + nombre_archivo)

def leer_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as f:
            contenido = f.read()
            print(contenido)
    except IOError:
        print("Error: no se pudo leer el archivo " + nombre_archivo)

def agregar_archivo(nombre_archivo, texto):
    try:
        with open(nombre_archivo, 'a') as f:
            f.write(texto)
        print("Texto añadido al archivo " + nombre_archivo + " exitosamente.")
    except IOError:
        print("Error: no se pudo agregar al archivo " + nombre_archivo)

def renombrar_archivo(nombre_archivo, nuevo_nombre_archivo):
    try:
        os.rename(nombre_archivo, nuevo_nombre_archivo)
        print("Archivo " + nombre_archivo + " renombrado a " + nuevo_nombre_archivo + " exitosamente.")
    except IOError:
        print("Error: no se pudo renombrar el archivo " + nombre_archivo)

def eliminar_archivo(nombre_archivo):
    try:
        os.remove(nombre_archivo)
        print("Archivo " + nombre_archivo + " eliminado exitosamente.")
    except IOError:
        print("Error: no se pudo eliminar el archivo " + nombre_archivo)

if __name__ == '__main__':
    nombre_archivo = "ejemplo.txt"
    nuevo_nombre_archivo = "nuevo_ejemplo.txt"

    crear_archivo(nombre_archivo)
    leer_archivo(nombre_archivo)
    agregar_archivo(nombre_archivo, "Este es un texto adicional.\n")
    leer_archivo(nombre_archivo)
    renombrar_archivo(nombre_archivo, nuevo_nombre_archivo)
    leer_archivo(nuevo_nombre_archivo)
    eliminar_archivo(nuevo_nombre_archivo)
