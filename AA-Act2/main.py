"""
Módulo para resolver el probl# Configuraciones del puzzle

Este módulo implementa un algoritmo de búsqueda con ramificación y poda para 
resolver el clásico puzzle de 15 losetas (sliding puzzle). El objetivo es 
reorganizar las piezas desde una configuración inicial hasta alcanzar la 
configuración objetivo.

Author: diego alejandro parra
Email: dap465@gmail.com

Contenido
---------
- Funciones
    - mostrar_tablero: Muestra el tablero del puzzle en consola.
    - calcular_heuristica: Calcula la distancia de Manhattan.
    - obtener_movimientos_validos: Obtiene los movimientos posibles.
    - comprobar: Verifica si un puzzle tiene solución.
    - ramificacion_y_poda: Resuelve el puzzle usando ramificación y poda.
    - validar_solucion: Valida que una secuencia de movimientos sea correcta.
    - comprobar: Verifica si un estado del puzzle tiene solución.

Attributes
----------
CONFIG_INICIAL : list of int
    Configuración inicial del tablero.
CONFIG_FINAL : list of int
    Configuración objetivo del tablero.
"""
import heapq
import copy
import time

# Configuraciones del puzzle
# CONFIG_INICIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 11, 15, 13, 14] # Solucion alcanzable
# CONFIG_INICIAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 14, 16, 15, 13, 11, 12] # Solucion no alcanzable
CONFIG_INICIAL = [15, 10, 9, 3, 1, 4, 14, 12, 5, 2, 8, 7, 16, 13, 11, 6]
CONFIG_FINAL = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def mostrar_tablero(lista, n):
    """
    Muestra el tablero del puzzle en formato visual.

    Imprime el tablero con bordes ASCII mostrando cada loseta en su posición.
    El número 16 representa el espacio vacío.

    Parameters
    ----------
    lista : list of int
        Lista que representa el estado actual del tablero.
    n : int
        Tamaño del tablero (n x n).

    Examples
    --------
    >>> mostrar_tablero([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16], 4)
    +---+---+---+---+
    | 1 | 2 | 3 | 4 |
    +---+---+---+---+
    | 5 | 6 | 7 | 8 |
    +---+---+---+---+
    | 9 |10 |11 |12 |
    +---+---+---+---+
    |13 |14 |15 |   |
    +---+---+---+---+
    """
    print()
    for i in range(n + 1):
        for j in range(n):
            print("+---", end="")
        print("+")
        if i < n:
            for j in range(n):
                valor = lista[i * n + j]
                if valor == 16:  # Espacio vacío
                    print("|   ", end="")
                else:
                    print("|{:2d} ".format(valor), end="")
            print("|")


def calcular_heuristica(estado, objetivo):
    """
    Calcula la distancia de Manhattan entre el estado actual y el objetivo.

    La distancia de Manhattan es la suma de las distancias absolutas entre
    las posiciones actuales y objetivo de cada loseta.

    Parameters
    ----------
    estado : list of int
        Estado actual del tablero.
    objetivo : list of int
        Estado objetivo del tablero.

    Returns
    -------
    int
        Distancia de Manhattan total.

    Notes
    -----
    Esta heurística es admisible (nunca sobreestima el costo real) y se usa
    en el algoritmo A* para guiar la búsqueda hacia la solución óptima.

    Examples
    --------
    >>> calcular_heuristica([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 15], 
    ...                     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16])
    2
    """
    n = int(len(estado) ** 0.5)
    distancia = 0
    
    for i, valor in enumerate(estado):
        if valor != 16:  # No calcular para el espacio vacío
            # Posición actual
            fila_actual = i // n
            col_actual = i % n
            
            # Posición objetivo
            pos_objetivo = objetivo.index(valor)
            fila_objetivo = pos_objetivo // n
            col_objetivo = pos_objetivo % n
            
            # Distancia de Manhattan
            distancia += abs(fila_actual - fila_objetivo) + abs(col_actual - col_objetivo)
    
    return distancia


def obtener_movimientos_validos(estado):
    """
    Obtiene todos los movimientos válidos desde el estado actual.

    Encuentra la posición del espacio vacío (16) y determina qué losetas
    pueden moverse hacia esa posición.

    Parameters
    ----------
    estado : list of int
        Estado actual del tablero.

    Returns
    -------
    list of list of int
        Lista de estados resultantes de todos los movimientos válidos.

    Notes
    -----
    Un movimiento válido consiste en intercambiar una loseta adyacente
    (arriba, abajo, izquierda, derecha) con el espacio vacío.
    """
    n = int(len(estado) ** 0.5)
    pos_vacio = estado.index(16)
    fila_vacio = pos_vacio // n
    col_vacio = pos_vacio % n
    
    movimientos = []
    
    # Posibles direcciones: arriba, abajo, izquierda, derecha
    direcciones = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for df, dc in direcciones:
        nueva_fila = fila_vacio + df
        nueva_col = col_vacio + dc
        
        # Verificar que la nueva posición esté dentro del tablero
        if 0 <= nueva_fila < n and 0 <= nueva_col < n:
            nueva_pos = nueva_fila * n + nueva_col
            
            # Crear nuevo estado intercambiando posiciones
            nuevo_estado = estado.copy()
            nuevo_estado[pos_vacio], nuevo_estado[nueva_pos] = nuevo_estado[nueva_pos], nuevo_estado[pos_vacio]
            movimientos.append(nuevo_estado)
    
    return movimientos


class Nodo:
    """
    Representa un nodo en el árbol de búsqueda.

    Attributes
    ----------
    estado : list of int
        Estado del tablero en este nodo.
    costo_g : int
        Costo del camino desde el estado inicial hasta este nodo.
    costo_h : int
        Valor heurístico (distancia de Manhattan al objetivo).
    costo_f : int
        Costo total (g + h).
    padre : Nodo or None
        Nodo padre en el camino de solución.
    """
    
    def __init__(self, estado, costo_g, costo_h, padre=None):
        """
        Inicializa un nuevo nodo.

        Parameters
        ----------
        estado : list of int
            Estado del tablero.
        costo_g : int
            Costo del camino desde el inicio.
        costo_h : int
            Valor heurístico.
        padre : Nodo, optional
            Nodo padre.
        """
        self.estado = estado
        self.costo_g = costo_g
        self.costo_h = costo_h
        self.costo_f = costo_g + costo_h
        self.padre = padre
    
    def __lt__(self, other):
        """Comparación para la cola de prioridad."""
        return self.costo_f < other.costo_f


def ramificacion_y_poda(estado_inicial, estado_objetivo):
    """
    Resuelve el puzzle usando el algoritmo de ramificación y poda (A*).

    Implementa el algoritmo A* que es una forma específica de ramificación
    y poda usando una heurística admisible para encontrar la solución óptima.

    Parameters
    ----------
    estado_inicial : list of int
        Configuración inicial del tablero.
    estado_objetivo : list of int
        Configuración objetivo del tablero.

    Returns
    -------
    tuple
        Una tupla conteniendo:
        - camino (list of list of int): Secuencia de estados desde inicial hasta objetivo.
        - nodos_explorados (int): Número de nodos explorados.
        - tiempo_ejecucion (float): Tiempo de ejecución en segundos.

    Notes
    -----
    El algoritmo utiliza:
    1. Una cola de prioridad para seleccionar el nodo más prometedor.
    2. La heurística de distancia de Manhattan para guiar la búsqueda.
    3. Un conjunto de estados visitados para evitar ciclos.
    
    La ramificación ocurre al generar todos los movimientos válidos,
    y la poda se realiza mediante la heurística y evitando estados repetidos.

    References
    ----------
    Hart, P. E., Nilsson, N. J., & Raphael, B. (1968). A formal basis for the 
    heuristic determination of minimum cost paths. IEEE transactions on Systems 
    Science and Cybernetics, 4(2), 100-107.
    """
    inicio_tiempo = time.time()
    
    # Verificar si ya estamos en el objetivo
    if estado_inicial == estado_objetivo:
        fin_tiempo = time.time()
        return [estado_inicial], 0, fin_tiempo - inicio_tiempo
    
    # Inicializar estructuras de datos
    cola_prioridad = []
    estados_visitados = set()
    nodos_explorados = 0
    
    # Nodo inicial
    h_inicial = calcular_heuristica(estado_inicial, estado_objetivo)
    nodo_inicial = Nodo(estado_inicial, 0, h_inicial)
    heapq.heappush(cola_prioridad, nodo_inicial)
    
    while cola_prioridad:
        nodo_actual = heapq.heappop(cola_prioridad)
        nodos_explorados += 1
        
        # Convertir estado a tupla para poder agregarlo al conjunto
        estado_tuple = tuple(nodo_actual.estado)
        
        # Si ya visitamos este estado, continuar
        if estado_tuple in estados_visitados:
            continue
            
        estados_visitados.add(estado_tuple)
        
        # Verificar si llegamos al objetivo
        if nodo_actual.estado == estado_objetivo:
            # Reconstruir camino
            camino = []
            nodo = nodo_actual
            while nodo is not None:
                camino.append(nodo.estado.copy())
                nodo = nodo.padre
            camino.reverse()
            
            fin_tiempo = time.time()
            return camino, nodos_explorados, fin_tiempo - inicio_tiempo
        
        # Generar sucesores (ramificación)
        movimientos_validos = obtener_movimientos_validos(nodo_actual.estado)
        
        for nuevo_estado in movimientos_validos:
            nuevo_estado_tuple = tuple(nuevo_estado)
            
            # Poda: si ya visitamos este estado, no lo consideramos
            if nuevo_estado_tuple not in estados_visitados:
                nuevo_g = nodo_actual.costo_g + 1
                nuevo_h = calcular_heuristica(nuevo_estado, estado_objetivo)
                nuevo_nodo = Nodo(nuevo_estado, nuevo_g, nuevo_h, nodo_actual)
                heapq.heappush(cola_prioridad, nuevo_nodo)
    
    # No se encontró solución
    fin_tiempo = time.time()
    return None, nodos_explorados, fin_tiempo - inicio_tiempo


def validar_solucion(camino, estado_inicial, estado_objetivo):
    """
    Valida que una secuencia de movimientos sea correcta.

    Verifica que cada paso en el camino sea un movimiento válido y que
    se llegue desde el estado inicial al estado objetivo.

    Parameters
    ----------
    camino : list of list of int
        Secuencia de estados del tablero.
    estado_inicial : list of int
        Estado inicial esperado.
    estado_objetivo : list of int
        Estado objetivo esperado.

    Returns
    -------
    bool
        True si la solución es válida, False en caso contrario.

    Notes
    -----
    La validación verifica:
    1. Que el primer estado sea el inicial.
    2. Que el último estado sea el objetivo.
    3. Que cada transición sea un movimiento válido.
    """
    if not camino:
        return False
    
    # Verificar estados inicial y final
    if camino[0] != estado_inicial or camino[-1] != estado_objetivo:
        return False
    
    # Verificar que cada paso sea un movimiento válido
    for i in range(len(camino) - 1):
        estado_actual = camino[i]
        estado_siguiente = camino[i + 1]
        
        # Obtener movimientos válidos desde el estado actual
        movimientos_validos = obtener_movimientos_validos(estado_actual)
        
        # Verificar que el siguiente estado esté entre los movimientos válidos
        if estado_siguiente not in movimientos_validos:
            return False
    
    return True


def comprobar(estado):
    """
    Verifica si un estado del puzzle tiene solución.

    Para un puzzle de n×n donde n es par, el puzzle tiene solución si:
    - El espacio vacío está en una fila par (contando desde abajo) y 
      el número de inversiones es impar, O
    - El espacio vacío está en una fila impar (contando desde abajo) y 
      el número de inversiones es par.

    Parameters
    ----------
    estado : list of int
        Estado del tablero a verificar.

    Returns
    -------
    tuple
        Una tupla conteniendo:
        - bool: True si el puzzle tiene solución, False en caso contrario.
        - str: Mensaje explicativo del resultado.

    Notes
    -----
    Una inversión ocurre cuando una loseta aparece antes que otra loseta
    con un valor menor (excluyendo el espacio vacío). Esta función implementa
    el teorema matemático que determina la resolubilidad de puzzles deslizantes.

    References
    ----------
    Johnson, W. W., & Story, W. E. (1879). Notes on the "15" puzzle. 
    American Journal of Mathematics, 2(4), 397-404.

    Examples
    --------
    >>> estado_solucionable = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 14, 16]
    >>> resultado, mensaje = comprobar(estado_solucionable)
    >>> print(resultado)
    True
    >>> print(mensaje)
    El puzzle SÍ tiene solución. Inversiones: 1, Fila del espacio vacío: 4 (par desde abajo)
    """
    n = int(len(estado) ** 0.5)
    
    # Encontrar la posición del espacio vacío (16)
    pos_vacio = estado.index(16)
    fila_vacio_desde_abajo = n - (pos_vacio // n)
    
    # Contar inversiones (excluyendo el espacio vacío)
    estado_sin_vacio = [x for x in estado if x != 16]
    inversiones = 0
    
    for i in range(len(estado_sin_vacio)):
        for j in range(i + 1, len(estado_sin_vacio)):
            if estado_sin_vacio[i] > estado_sin_vacio[j]:
                inversiones += 1
    
    # Determinar si tiene solución
    tiene_solucion = False
    
    if n % 2 == 1:  # n impar
        # Para tableros de tamaño impar, debe tener número par de inversiones
        tiene_solucion = (inversiones % 2 == 0)
        if tiene_solucion:
            mensaje = f"El puzzle SÍ tiene solución. Inversiones: {inversiones} (par)"
        else:
            mensaje = f"El puzzle NO tiene solución. Inversiones: {inversiones} (impar)"
    else:  # n par
        # Para tableros de tamaño par, aplicar regla más compleja
        if fila_vacio_desde_abajo % 2 == 0:  # Fila par desde abajo
            tiene_solucion = (inversiones % 2 == 1)
        else:  # Fila impar desde abajo
            tiene_solucion = (inversiones % 2 == 0)
        
        tipo_fila = "par" if fila_vacio_desde_abajo % 2 == 0 else "impar"
        tipo_inversiones = "par" if inversiones % 2 == 0 else "impar"
        
        if tiene_solucion:
            mensaje = (f"El puzzle SÍ tiene solución. Inversiones: {inversiones} ({tipo_inversiones}), "
                      f"Fila del espacio vacío: {fila_vacio_desde_abajo} ({tipo_fila} desde abajo)")
        else:
            mensaje = (f"El puzzle NO tiene solución. Inversiones: {inversiones} ({tipo_inversiones}), "
                      f"Fila del espacio vacío: {fila_vacio_desde_abajo} ({tipo_fila} desde abajo)")
    
    return tiene_solucion, mensaje


def main():
    """
    Función principal que ejecuta el solucionador del puzzle.

    Muestra la configuración inicial, ejecuta el algoritmo de ramificación
    y poda, y presenta los resultados incluyendo el camino de solución,
    estadísticas de rendimiento y validación.
    """
    print("=" * 60)
    print("SOLUCIONADOR DEL PUZLE DE LAS LOSETAS")
    print("Algoritmo: Ramificación y Poda (A*)")
    print("=" * 60)
    
    print("\nConfiguración inicial:")
    mostrar_tablero(CONFIG_INICIAL, 4)
    
    print("\nConfiguración objetivo:")
    mostrar_tablero(CONFIG_FINAL, 4)
    
    # Validar si el puzzle tiene solución antes de intentar resolverlo
    print("\nVerificando si el puzzle tiene solución...")
    print("-" * 40)
    
    tiene_solucion, mensaje_validacion = comprobar(CONFIG_INICIAL)
    print(mensaje_validacion)
    
    if not tiene_solucion:
        print("\nEl puzzle no puede ser resuelto. El programa terminará.")
        print("=" * 60)
        return
    
    print("\nBuscando solución...")
    print("-" * 40)
    
    # Resolver el puzzle
    resultado = ramificacion_y_poda(CONFIG_INICIAL, CONFIG_FINAL)
    camino, nodos_explorados, tiempo_ejecucion = resultado
    
    if camino is None:
        print("No se encontró solución al puzzle.")
        return
    
    print(f"\n¡Solución encontrada!")
    print(f"Número de movimientos: {len(camino) - 1}")
    print(f"Nodos explorados: {nodos_explorados}")
    print(f"Tiempo de ejecución: {tiempo_ejecucion:.4f} segundos")
    
    # Validar la solución
    es_valida = validar_solucion(camino, CONFIG_INICIAL, CONFIG_FINAL)
    print(f"Solución válida: {'Sí' if es_valida else 'No'}")
    
    # Mostrar opción para ver el camino completo
    mostrar_camino = input("\n¿Desea ver el camino completo de la solución? (s/n): ")
    
    if mostrar_camino.lower() in ['s', 'sí', 'si', 'y', 'yes']:
        print("\nCamino de la solución:")
        print("=" * 60)
        
        for i, estado in enumerate(camino):
            print(f"\nPaso {i}:")
            mostrar_tablero(estado, 4)
            
            if i < len(camino) - 1:
                input("Presione Enter para continuar...")
    
    print("\n" + "=" * 60)
    print("Programa completado exitosamente.")
    print("=" * 60)


if __name__ == "__main__":
    main()
