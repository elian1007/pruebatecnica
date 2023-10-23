import sys

# en la terminal ejecutamos python inicial.py archivo.txt (nombre del archivo a ejecutar)
# N (le indicamos la cantidad)
def imprimir_primeras_n_lineas(archivo, n):
    try:
        with open(archivo, 'r', encoding='utf-8') as file:
            for i, linea in enumerate(file):
                if i < n:
                    print(linea.strip())
                else:
                    break
    except FileNotFoundError:
        print(f"El archivo '{archivo}' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python inicial.py archivo.txt N")
    else:
        archivo = sys.argv[1]
        n = int(sys.argv[2])
        imprimir_primeras_n_lineas(archivo, n)
