Laboratorio #1: Par más cercano

**Descripción del laboratorio**

El problema del "par más cercano" consiste en encontrar, dado un conjunto de puntos en un plano bidimensional, los dos puntos que tienen la menor distancia euclidiana entre ellos.

Según el documento:

Se te proporcionará un conjunto de datos de entrada en un archivo de texto (.txt), donde cada línea representa un punto con coordenadas (x, y).
Tu programa debe identificar los dos puntos (P(x₁, y₁) y Q(x₂, y₂)) que están más cerca el uno del otro.
Además, debe calcular la distancia mínima entre estos dos puntos.
La solución debe implementarse utilizando la estrategia de "divide y conquista".

Durante este laboratorio nos familiarizaremos con Python.

Después deberá resolver el problema planteado en el laboratorio aplicando la estrategia divide y conquista y construir un programa que muestre la solución.

**Entrega del laboratorio**

Una vez acabado el trabajo, adjunto un fichero donde se implementen las funciones. Indique si funciona bien tu programa, y qué fallos existen.

**Revisión del laboratorio**

La revisión de las actividades calificables no se realizar por el foro, debe realizarse a través del tutor.

**Salida:**

Se muestra en consola:

- Los pares más cercanos: .

$$
P(x_1, y_1) y Q(x_2, y_2)
$$

- La distancia mínima.
- El tiempo de ejecución.a

---

**Criterios de evaluación:**

- **(60%)** El programa escrito en Python y entregado en un único archivo con extensión .py lee el archivo plano con extensión .txt que contiene el conjunto de datos de entrada. Se pueden realizar pruebas con conjuntos de datos de diferente tamaño (100, 1000, 10000,…). Se presenta en la consola la salida requerida: los dos pares más cercanos del conjunto de datos, la distancia euclidiana entre ellos y el tiempo de ejecución. La solución se basa en la estrategia divide y conquista. En la documentación del programa se indica cómo está implementada esta estrategia.
- **(20%)** La documentación del programa se realiza de acuerdo con el estilo NumPy para docstring. Se espera como mínimo el uso de las siguientes secciones: short summary, extended summary, parameters, returns, notes, references y examples.
- **(20%)** El programa está libre de problemas de estilo, malas prácticas y errores. El análisis se realizará en Spyder con **Pylint**. Si la evaluación global es inferior a 8 sobre 10, se restará 1 unidad; pero si es inferior a 5 sobre 10, se restarán 2 unidades.

---

**Interés práctico***:

Gráficas, visión por computador, sistemas de información geográfica, simulación molecular, control de tráfico aéreo…

(*) Ruzzo, L. (s.f.). CSE 521. *Algorithms: Divide and Conquer*. P. 13. Recuperado de

https://courses.cs.washington.edu/courses/cse521/13wi/slides/05dc.pdf

---

### **Mejorando la solución: divide y conquista**

- **Parte 1: divide**
    
    (dos conjuntos con n/2 puntos aproximadamente) → *ordenar en un eje*
    
- **Parte 2: conquista**
    
    (encontrar el par más cercano en cada conjunto, recursivamente)
    
- **Parte 3: combina**
    
    (encontrar el par más cercano, con un punto en cada conjunto)
    

Platilla de documentacion de funciones 

```python
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

    References
    ----------
    Ruzzo, L. (s.f.). *CSE 521: Algorithms - Divide and Conquer*, p. 13.  
    Recuperado de: https://courses.cs.washington.edu/courses/cse521/13wi/slides/05dc.pdf

    Examples
    --------
    Suponiendo un archivo `puntos.txt` con el contenido:
    1,2  
    3,4  
    5,6

    >>> leer_puntos("puntos.txt")
    [(1, 2), (3, 4), (5, 6)]
    """
    with open(nombre_archivo, 'r') as archivo:
        return [tuple(map(int, linea.strip().split(','))) for linea in archivo]
```

Plantilla para documentar un modulo

```python
"""
Nombre del módulo o una descripción breve.

Descripción más extensa del propósito del módulo, su contexto y sus características principales.
Puede incluir cómo se relaciona con otros módulos o su rol dentro del proyecto.

Contenido
---------
- Funciones
- Clases
- Constantes
- Excepciones (si aplica)

Attributes
----------
NOMBRE_CONSTANTE : tipo
    Descripción de la constante o atributo global, si aplica.

Notes
-----
Notas adicionales sobre implementación, advertencias o contexto histórico.

References
----------
Referencia a artículos, libros, enlaces o documentación adicional.

Examples
--------
Ejemplo de uso del módulo:

>>> from mi_modulo import funcion_principal
>>> resultado = funcion_principal("datos.txt")
>>> print(resultado)
"""

# Imports (van después del docstring)
import math
import os

# Constantes
PI = 3.14159

# Funciones
def funcion_principal(...):
    ...
```