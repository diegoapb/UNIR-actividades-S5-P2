"""
Módulo para visualizar un conjunto de puntos en un plano 2D.

Lee puntos desde un archivo de texto y los grafica usando Matplotlib.
"""
import matplotlib.pyplot as plt
# Asumimos que main.py está en el mismo directorio o en el PYTHONPATH
# para poder importar leer_puntos.
# Si no, copia la función leer_puntos aquí o ajusta la importación.
from main import leer_puntos

def graficar_puntos(nombre_archivo_datos, nombre_archivo_salida="puntos_visualizados.png"):
    """
    Lee puntos de un archivo y genera un gráfico de dispersión.

    Parameters
    ----------
    nombre_archivo_datos : str
        Ruta del archivo de texto que contiene los datos de los puntos.
    nombre_archivo_salida : str, optional
        Nombre del archivo donde se guardará el gráfico.
        Por defecto es "puntos_visualizados.png".
    """
    try:
        puntos = leer_puntos(nombre_archivo_datos)
    except FileNotFoundError:
        print(f"Error: El archivo de datos '{nombre_archivo_datos}' no fue encontrado.")
        return
    except Exception as e:
        print(f"Ocurrió un error al leer los puntos: {e}")
        return

    if not puntos:
        print("No se encontraron puntos para graficar.")
        return

    # Separar las coordenadas x e y
    x_coords = [p[0] for p in puntos]
    y_coords = [p[1] for p in puntos]

    plt.figure(figsize=(10, 8))
    plt.scatter(x_coords, y_coords, s=10)  # s es el tamaño del punto
    plt.title(f"Visualización de Puntos del Archivo: {nombre_archivo_datos}")
    plt.xlabel("Coordenada X")
    plt.ylabel("Coordenada Y")
    plt.grid(True)
    
    try:
        plt.savefig(nombre_archivo_salida)
        print(f"Gráfico guardado como '{nombre_archivo_salida}'")
    except Exception as e:
        print(f"Error al guardar el gráfico: {e}")

if __name__ == "__main__":
    # Puedes cambiar este nombre de archivo al que quieras visualizar
    archivo_a_visualizar = "/Users/parra/Documents/AP/unir/Fisica2/algoritmos-avanzados/datos_10000.txt" 
    # archivo_a_visualizar = "datos_1000.txt"
    # archivo_a_visualizar = "datos_10000.txt"
    
    print(f"Generando gráfico para el archivo: {archivo_a_visualizar}")
    graficar_puntos(archivo_a_visualizar)
