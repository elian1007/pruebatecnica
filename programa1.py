import sys
import mysql.connector
from datetime import datetime
# en la terminal ejecutamos python inicial.py archivo.txt (nombre del archivo a ejecutar)

# Función para contar líneas, palabras y caracteres en un archivo
def contar_archivo(archivo):
   with open(archivo, 'r', encoding='utf-8') as file:  # Utiliza 'utf-8' para abrir archivos
       contenido = file.read()
       cant_lineas = len(contenido.split('\n'))
       cant_palabras = len(contenido.split())
       cant_caracteres = len(contenido)
       return cant_lineas, cant_palabras, cant_caracteres

def guardar_en_mysql(archivo, cant_lineas, cant_palabras, cant_caracteres):
   try:
       connection = mysql.connector.connect(
           host="localhost",
           user="root",
           password="",
           database="datosdb",
       )

       cursor = connection.cursor()
       fecha_registro = datetime.now()

       insert_query = "INSERT INTO informacion (nombrearchivo, cantlineas, cantpalabras, cantcaracteres, fecharegistro) VALUES (%s, %s, %s, %s, %s)"
       data = (archivo, cant_lineas, cant_palabras, cant_caracteres, fecha_registro)

       cursor.execute(insert_query, data)
       connection.commit()
       print("Datos guardados en la base de datos.")
   except Exception as e:
       print(f"Ocurrió un error al guardar en la base de datos: {str(e)}")
   finally:
       if 'cursor' in locals():
           cursor.close()
       if 'connection' in locals():
           connection.close()

if __name__ == "__main__":
   if len(sys.argv) != 2:
       print("Uso: python programa1.py archivo.txt")
   else:
       archivo = sys.argv[1]
       cant_lineas, cant_palabras, cant_caracteres = contar_archivo(archivo)
       guardar_en_mysql(archivo, cant_lineas, cant_palabras, cant_caracteres)
