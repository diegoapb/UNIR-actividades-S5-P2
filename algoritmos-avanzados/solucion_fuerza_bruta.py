"""
Módulo para calcular el par de puntos más cercano usando la estrategia 
divide y conquista.

Este módulo incluye funciones para leer coordenadas desde un archivo de texto
plano y calcular eficientemente la distancia mínima entre pares de puntos.
"""

import math
import time

def distancia(p, q):
    d = math.sqrt((q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)
    return d

def fuerza_bruta(lista_pares):
    num_pares = len(lista_pares)
    dis_minima = math.inf
    pares_cercanos = []
    for i in range(num_pares):
        for j in range(i + 1, num_pares):
            dis_temporal = distancia(lista_pares[i], lista_pares[j])
            if dis_temporal < dis_minima:
                dis_minima = dis_temporal
                pares_cercanos = [lista_pares[i], lista_pares[j]]
    return pares_cercanos, dis_minima

def leer_tuplas(nombre_archivo):
    """
    Lee dos líneas de un archivo de texto y devuelve una lista de tuplas.
   
    Cada línea del archivo debe contener una secuencia de números separados por
    coma.

    Parámetros
    ----------
    nombre_archivo : str
        Ruta del archivo de texto que contiene los datos.

    Returns
    -------
    list
        Lista de tuplas con pares de números enteros.
        
    
    Notes
    -----
    
    References
    ----------
    
    Examples
    --------
    >>> leer_tuplas("datos.txt")
    [(1, 4), (2, 5), (3, -6)]
    
    """
    with open(nombre_archivo, encoding="utf-8") as datos:
        x = list(map(int, datos.readline().split(",")))
        y = list(map(int, datos.readline().split(",")))
    return list(zip(x, y))


lista = leer_tuplas("datos_100.txt")
inicio1 = time.time()
pares, dist = fuerza_bruta(lista)
fin1 = time.time()

print("Los pares más cercanos son {} y {}.".format(pares[0], pares[1]))
print("La distancia entre ellos es {:.3f}".format(dist))
print("El tiempo de ejecución fue de {:.3f} s.".format(fin1 - inicio1))
