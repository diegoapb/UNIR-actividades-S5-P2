"""
Módulo para encontrar el par de puntos más cercano en un plano bidimensional.

Este módulo implementa el algoritmo de divide y conquista para resolver el
problema del par más cercano. Lee un conjunto de puntos desde un archivo de
texto, calcula la distancia euclidiana entre todos los pares de puntos y
encuentra el par con la distancia mínima.

Contenido
---------
- Funciones
    - leer_puntos: Lee puntos desde un archivo.
    - calcular_distancia: Calcula la distancia euclidiana entre dos puntos.
    - par_mas_cercano_fuerza_bruta: Encuentra el par más cercano usando fuerza bruta.
    - par_mas_cercano_div_conq: Encuentra el par más cercano usando divide y conquista.
    - encontrar_par_mas_cercano: Función principal que coordina la solución.
"""
import math
import time

def leer_puntos(nombre_archivo):
    """
    Lee un archivo de texto y devuelve una lista de tuplas de enteros.

    Cada línea del archivo debe contener una secuencia de dos números enteros
    separados por coma, representando coordenadas en un plano bidimensional.

    Parameters
    ----------
    nombre_archivo : str
        Ruta del archivo de texto que contiene los datos.

    Returns
    -------
    list of tuple of int
        Lista de tuplas, cada una con un par de enteros representando coordenadas (x, y).

    Notes
    -----
    - Se asume que el archivo tiene formato válido y no contiene líneas vacías.
    - Si una línea no contiene exactamente dos valores separados por coma,
    puede generar una excepción.

    Examples
    --------
    Suponiendo un archivo `puntos.txt` con el contenido:
    1,3,5,...
    2,4,6,...

    >>> leer_puntos("puntos.txt")
    [(1, 2), (3, 4), (5, 6)]
    """
    with open(nombre_archivo) as datos:
        x = list(map(int, datos.readline().split(",")))
        y = list(map(int, datos.readline().split(",")))
    return list(zip(x, y))

def calcular_distancia(punto1, punto2):
    """
    Calcula la distancia euclidiana entre dos puntos en un plano 2D.

    Parameters
    ----------
    punto1 : tuple of int
        Una tupla (x, y) representando el primer punto.
    punto2 : tuple of int
        Una tupla (x, y) representando el segundo punto.

    Returns
    -------
    float
        La distancia euclidiana entre los dos puntos.

    Examples
    --------
    >>> calcular_distancia((1, 2), (4, 6))
    5.0
    """
    return math.sqrt((punto1[0] - punto2[0])**2 + (punto1[1] - punto2[1])**2)

def par_mas_cercano_fuerza_bruta(puntos):
    """
    Encuentra el par de puntos más cercano usando un enfoque de fuerza bruta.

    Este método se utiliza como caso base para la recursión en el algoritmo
    de divide y conquista cuando el número de puntos es pequeño.

    Parameters
    ----------
    puntos : list of tuple of int
        Lista de puntos, donde cada punto es una tupla (x, y).

    Returns
    -------
    tuple
        Una tupla conteniendo:
        - punto1 (tuple of int): El primer punto del par más cercano.
        - punto2 (tuple of int): El segundo punto del par más cercano.
        - min_dist (float): La distancia mínima entre los dos puntos.
        Retorna (None, None, float('inf')) si hay menos de dos puntos.

    Notes
    -----
    La complejidad de este algoritmo es O(n^2), donde n es el número de puntos.
    Es eficiente para un número pequeño de puntos (por ejemplo, n <= 3).
    """
    n = len(puntos)
    if n < 2:
        return None, None, float('inf')

    min_dist = float('inf')
    par_cercano = (None, None)

    for i in range(n):
        for j in range(i + 1, n):
            dist = calcular_distancia(puntos[i], puntos[j])
            if dist < min_dist:
                min_dist = dist
                par_cercano = (puntos[i], puntos[j])
    return par_cercano[0], par_cercano[1], min_dist

def par_mas_cercano_div_conq_recursivo(puntos_ordenados_x, puntos_ordenados_y):
    """
    Encuentra el par de puntos más cercano usando la estrategia de divide y conquista.

    Esta es la función recursiva principal del algoritmo.

    Parameters
    ----------
    puntos_ordenados_x : list of tuple of int
        Lista de puntos ordenados por su coordenada x.
    puntos_ordenados_y : list of tuple of int
        Lista de puntos ordenados por su coordenada y.

    Returns
    -------
    tuple
        Una tupla conteniendo:
        - punto1 (tuple of int): El primer punto del par más cercano.
        - punto2 (tuple of int): El segundo punto del par más cercano.
        - min_dist (float): La distancia mínima entre los dos puntos.

    Notes
    -----
    El algoritmo sigue los pasos de divide, conquista y combina:
    1. Divide: Divide el conjunto de puntos en dos mitades por una línea vertical.
    2. Conquista: Recursivamente encuentra el par más cercano en cada mitad.
    3. Combina: Encuentra el par más cercano donde los puntos están en diferentes mitades.
    Esto implica considerar puntos dentro de una "franja" alrededor de la línea divisoria.
    """
    n = len(puntos_ordenados_x)

    # Caso base: si hay pocos puntos, usar fuerza bruta
    if n <= 3:
        return par_mas_cercano_fuerza_bruta(puntos_ordenados_x)

    # 1. Divide
    medio = n // 2
    punto_medio = puntos_ordenados_x[medio]

    # Dividir puntos_ordenados_y en p_y_izq y p_y_der
    p_y_izq = []
    p_y_der = []
    for p in puntos_ordenados_y:
        if p[0] < punto_medio[0] or (p[0] == punto_medio[0] and p[1] < punto_medio[1]):
            p_y_izq.append(p)
        else:
            p_y_der.append(p)
    
    # 2. Conquista
    p1_izq, p2_izq, dist_izq = par_mas_cercano_div_conq_recursivo(puntos_ordenados_x[:medio], p_y_izq)
    p1_der, p2_der, dist_der = par_mas_cercano_div_conq_recursivo(puntos_ordenados_x[medio:], p_y_der)

    # Determinar la distancia mínima de las sub-soluciones
    if dist_izq <= dist_der:
        d_min = dist_izq
        par_min = (p1_izq, p2_izq)
    else:
        d_min = dist_der
        par_min = (p1_der, p2_der)

    # 3. Combina
    # Crear una franja de puntos cuya distancia x al punto medio sea menor que d_min
    franja = []
    for punto in puntos_ordenados_y:
        if abs(punto[0] - punto_medio[0]) < d_min:
            franja.append(punto)

    # Buscar el par más cercano en la franja
    # Los puntos en 'franja' ya están ordenados por y
    tam_franja = len(franja)
    for i in range(tam_franja):
        for j in range(i + 1, tam_franja):
            # Optimización: solo comparar puntos si su diferencia en y es menor que d_min
            if (franja[j][1] - franja[i][1]) >= d_min:
                break
            dist = calcular_distancia(franja[i], franja[j])
            if dist < d_min:
                d_min = dist
                par_min = (franja[i], franja[j])

    return par_min[0], par_min[1], d_min

def encontrar_par_mas_cercano(puntos):
    """
    Función envoltorio para iniciar el algoritmo de divide y conquista.

    Prepara los datos ordenando los puntos por las coordenadas (x , y)
    antes de llamar a la función recursiva.

    Parameters
    ----------
    puntos : list of tuple of int
        Lista de puntos, donde cada punto es una tupla (x, y).

    Returns
    -------
    tuple
        Una tupla conteniendo:
        - punto1 (tuple of int): El primer punto del par más cercano.
        - punto2 (tuple of int): El segundo punto del par más cercano.
        - min_dist (float): La distancia mínima entre los dos puntos.

    References
    ----------
    Adaptado del algoritmo descrito en Cormen, T. H., Leiserson, C. E.,
    Rivest, R. L., & Stein, C. (2009). *Introduction to Algorithms*. MIT Press.
    """
    n = len(puntos)
    if n < 2:
        return None, None, float('inf')

    puntos_ordenados_x = sorted(puntos, key=lambda p: p[0])
    puntos_ordenados_y = sorted(puntos, key=lambda p: p[1])

    return par_mas_cercano_div_conq_recursivo(puntos_ordenados_x, puntos_ordenados_y)

if __name__ == "__main__":
    # Ejemplo de uso:
    # Se espera que los archivos de datos estén en el mismo directorio o
    # se proporcione la ruta completa.
    ARCHIVOS = ["datos_100.txt", "datos_1000.txt", "datos_10000.txt"]
    # ARCHIVOS = ["datos_10000.txt"]
    for nombre_archivo_datos in ARCHIVOS:
        print(f"Procesando archivo: {nombre_archivo_datos}")
        
        try:
            puntos_leidos = leer_puntos(nombre_archivo_datos)
            if not puntos_leidos:
                print("No se leyeron puntos o el archivo está vacío.")
            else:
                print(f"Número de puntos leídos: {len(puntos_leidos)}")

                inicio_tiempo = time.time()
                punto_a, punto_b, distancia = encontrar_par_mas_cercano(puntos_leidos)
                fin_tiempo = time.time()
                tiempo_ejecucion = fin_tiempo - inicio_tiempo

                if punto_a and punto_b:
                    print(f"Los pares más cercanos son: P{punto_a} y Q{punto_b}")
                    print(f"La distancia mínima es: {distancia:.4f}")
                    print(f"El tiempo de ejecución fue: {tiempo_ejecucion:.6f} segundos.")
                else:
                    print("No se pudo encontrar un par más cercano (menos de 2 puntos).")

        except FileNotFoundError:
            print(f"Error: El archivo '{nombre_archivo_datos}' no fue encontrado.")
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
