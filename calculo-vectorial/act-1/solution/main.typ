#import "@preview/charged-ieee:0.1.3": ieee

#show: ieee.with(
  title: [Trabajo: Secciones cónicas y ecuaciones polares],
  abstract: [
    Este documento presenta la solución a una serie de ejercicios relacionados con secciones cónicas y ecuaciones polares. Se abordan problemas que implican la identificación y análisis de elipses, parábolas y otras curvas, determinando sus elementos característicos como focos, vértices y ejes, y aplicando estos conceptos a situaciones prácticas.
  ],
  authors: (
    (
      name: "Diego Alejandro Parra Bravo",
      department: [Cálculo Vectorial],
      organization: [Universidad Internacional de La Rioja],
      location: [Cali, Colombia],
      email: "dap465@gmail.com"
    ),
  ),
  // index-terms: ("Scientific writing", "Typesetting", "Document creation", "Syntax"),
  bibliography: bibliography("refs.bib"),
  // figure-supplement: [Fig.],
)

= Primer ejercicio <sec:ejercicio1>

Un haz de luz es emitido desde una fuente F1, este rayo se refleja dentro de un recinto elíptico, sin importar la dirección hacia donde apunte, siempre llegará a su receptor F2 (ver imagen). Considera el centroide en la coordenada C(30, 25), su eje mayor horizontal con una longitud de 80 cm y su eje menor vertical con 30cm de longitud. ¿Qué distancia separa a la fuente del receptor? Justifica tu respuesta y elabora una representación en el plano bidimensional ubicando los vértices, distancia entre focos y ejes.

== Solución

La propiedad fundamental de una elipse es que la suma de las distancias desde cualquier punto de la elipse a sus dos focos es constante. Además, un rayo emitido desde un foco (F1) se reflejará en la superficie de la elipse y pasará por el otro foco (F2). La fuente F1 y el receptor F2 son los focos de la elipse.

=== Datos proporcionados
- Centro de la elipse (C): $(h, k) = (30, 25)$
- Longitud del eje mayor horizontal ($2a$): $80 space "cm"$
- Longitud del eje menor vertical ($2b$): $30 space "cm"$

=== Cálculo de los semiejes
A partir de las longitudes de los ejes, calculamos los semiejes:
- Semieje mayor ($a$): $2a / 2 = 80 space "cm" / 2 = 40 space "cm"$
- Semieje menor ($b$): $2b / 2 = 30 space "cm" / 2 = 15 space "cm"$

=== Cálculo de la distancia del centro a los focos ($c$)
Para una elipse, la relación entre los semiejes $a$, $b$ y la distancia del centro a cada foco $c$ es:
$ a^2 = b^2 + c^2 $
Despejamos $c$:
$ c^2 = a^2 - b^2 $
$ c = sqrt(a^2 - b^2) $
Sustituyendo los valores:
$ c = sqrt((40 space "cm")^2 - (15 space "cm")^2) $
$ c = sqrt(1600 space "cm"^2 - 225 space "cm"^2) $
$ c = sqrt(1375 space "cm"^2) $
$ c approx 37.081 space "cm" $

=== Distancia entre la fuente (F1) y el receptor (F2)
La distancia que separa la fuente del receptor es la distancia entre los dos focos, que es $2c$.
$ "Distancia F1-F2" = 2c = 2 times sqrt(1375) space "cm" approx 2 times 37.081 space "cm" $
$ "Distancia F1-F2" approx 74.162 space "cm" $

*Conclusión: La distancia que separa a la fuente del receptor es aproximadamente $74.162 space "cm"$.*

=== Representación en el plano bidimensional

Para la representación, necesitamos las coordenadas de los vértices y los focos.
- Centro: $C = (30, 25)$

- Vértices del eje mayor (horizontales, ya que el eje mayor es horizontal):
  $ V_1 = (h - a, k) = (30 - 40, 25) = (-10, 25) $
  $ V_2 = (h + a, k) = (30 + 40, 25) = (70, 25) $

- Vértices del eje menor (co-vértices, verticales):
  $ B_1 = (h, k - b) = (30, 25 - 15) = (30, 10) $
  $ B_2 = (h, k + b) = (30, 25 + 15) = (30, 40) $

- Focos (sobre el eje mayor horizontal):
  $ F_1 = (h - c, k) $
  $ F_1 = (30 - sqrt(1375), 25) $
  $ F_1 approx (30 - 37.081, 25) $
  $ F_1 approx (-7.081, 25) $

  $ F_2 = (h + c, k) $
  $ F_2 = (30 + sqrt(1375), 25) $
  $ F_2 approx (30 + 37.081, 25) $
  $ F_2 approx (67.081, 25) $

La representación gráfica sería una elipse centrada en $(30, 25)$, con su eje mayor extendiéndose horizontalmente desde $x = -10$ hasta $x = 70$, y su eje menor extendiéndose verticalmente desde $y = 10$ hasta $y = 40$. Los focos F1 y F2 estarían ubicados en el eje mayor en las coordenadas aproximadas $(-7.081, 25)$ y $(67.081, 25)$ respectivamente.
La ecuación canónica de la elipse es:
$ ((x - 30)^2) / (40^2) + ((y - 25)^2) / (15^2) = 1 $

#image("image.png")

= Segundo ejercicio <sec:ejercicio2>

Un radiotelescopio es una antena de uso especializado para la captación de ondas de radio emitidas desde fuentes astronómicas (cuerpos celestes). Si la antena tiene un diámetro de 12 m y una profundidad de 3.6 m, ¿a qué altura se debe ubicar la primera cabina focal (ver imagen de referencia)? Elabora una representación en el plano bidimensional como una sección cónica junto con la posición focal y justifica tu respuesta.

#image("image-1.png")

== Solución

La forma de un radiotelescopio es parabólica. La propiedad de una parábola es que todas las ondas que llegan paralelas a su eje de simetría se reflejan y convergen en un único punto llamado foco. Es en este punto donde se debe ubicar el receptor (la cabina focal) para captar eficientemente las señales.

=== Datos proporcionados
- Diámetro de la antena ($D$): $12 space "m"$
- Profundidad de la antena ($h$): $3.6 space "m"$

=== Planteamiento del problema
Consideramos una sección transversal de la antena parabólica. Podemos situar el vértice de la parábola en el origen $(0,0)$ del plano cartesiano, con el eje de la parábola coincidiendo con el eje $y$. Dado que la antena se abre hacia arriba para recibir señales, la ecuación de la parábola es de la forma:
$ x^2 = 4"py" $
donde $p$ es la distancia del vértice al foco (y también del vértice a la directriz). La cabina focal debe ubicarse en el foco de la parábola, es decir, a una altura $p$ sobre el vértice.

=== Cálculo de la posición focal ($p$)
El diámetro de la antena es de $12 space "m"$.
La profundidad de la antena es de $3.6 space "m"$.
Entonces, el punto $(6, 3.6)$ pertenece a la parábola. Sustituimos estas coordenadas en la ecuación de la parábola:
$ (6 space "m")^2 = 4p (3.6 space "m") $
$ 36 space "m"^2 = 14.4 space "m" times p $
Despejamos $p$:
$ p = (36 space "m"^2) / (14.4 space "m") $
$ p = 2.5 space "m" $

La altura a la que se debe ubicar la primera cabina focal es $2.5 space "m"$ por encima del vértice de la antena.

* Conclusión: La cabina focal debe ubicarse a una altura de $2.5 space "m"$ desde el vértice (fondo) de la antena.*

=== Representación en el plano bidimensional
- Vértice de la parábola: $V = (0,0)$
- Ecuación de la parábola: $x^2 = 4(2.5)y = 10y$
- Foco de la parábola: $F = (0, p) = (0, 2.5)$
- Puntos en el borde de la antena: $(-6, 3.6)$ y $(6, 3.6)$

La representación gráfica sería una parábola con vértice en el origen, abriéndose hacia arriba, pasando por los puntos $(-6, 3.6)$ y $(6, 3.6)$. El foco estaría ubicado en el eje $y$ en el punto $(0, 2.5)$.

#image("image-2.png")

= Tercer ejercicio <sec:ejercicio3>

Observa el siguiente [video](https://youtu.be/yNgqI4XPUZc) donde se explica el funcionamiento de un compresor. Luego realiza la doble representación de las espirales de Arquímedes usando un entorno de programación de tu preferencia (Sugerencia: Google Colab). Debes incorporar un recorte de pantalla del código ejecutado, así como de las gráficas resultantes usando las ecuaciones en coordenadas polares.

== Solución

=== Espirales de Arquímedes y su relación con los compresores

Las espirales de Arquímedes son curvas geométricas descritas por un punto que se mueve a velocidad constante a lo largo de una línea que rota a velocidad angular constante @uchile_espiral. Estas espirales son fundamentales en el diseño de compresores scroll, como se muestra en el video referenciado.

En un compresor scroll, dos espirales idénticas encajan perfectamente: una fija y otra que orbita sin rotar. Este movimiento orbital crea bolsas de gas que se van reduciendo en volumen a medida que el gas avanza hacia el centro, comprimiéndolo en el proceso.

=== Ecuación polar de la espiral de Arquímedes

La ecuación polar de una espiral de Arquímedes está dada por:

$ r = a theta $

donde:
- $r$ es la distancia radial desde el origen.
- $a$ es una constante positiva que determina la separación entre los brazos sucesivos de la espiral.
- $ theta$ es el ángulo polar en radianes.

=== Doble representación de la espiral de Arquímedes

La "doble representación" de una espiral de Arquímedes se refiere a la visualización de dos espirales entrelazadas, que es precisamente lo que ocurre en un compresor scroll. Matemáticamente, esto se puede lograr de dos formas principales:

1. *Dos espirales con un desfase angular*: Graficando $r_1 = a theta$ y $r_2 = a( theta + \pi)$. Esto crea dos espirales que están desfasadas 180 grados.

2. *Rama positiva y negativa de la misma ecuación*: Graficando $r_1 = a theta$ y $r_2 = -a theta$ para el mismo rango positivo de $ theta$. Esto también crea dos brazos que se entrelazan.

=== Código para la representación gráfica
Se usa la segunda opción, con la rama positiva y negativa de la espiral de Arquímedes. A continuación se presenta el código en Python para graficar las dos espirales:
```python
import numpy as np
import matplotlib.pyplot as plt

# Parámetros
b = 0.3
theta = np.linspace(0, 8 * np.pi, 1000)

# Rama 1: r = b * theta
r1 = b * theta
x1 = r1 * np.cos(theta)
y1 = r1 * np.sin(theta)

# Rama 2: r = -b * theta
r2 = -b * theta
x2 = r2 * np.cos(theta)
y2 = r2 * np.sin(theta)

# Gráfico
plt.figure(figsize=(7, 7))
plt.plot(x1, y1, label=r"$r = b\theta$", linewidth=2)
plt.plot(x2, y2, label=r"$r = -b\theta$", linewidth=2, linestyle='--')
plt.title("Doble espiral de Arquímedes")
plt.xlabel("x")
plt.ylabel("y")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()
```
=== Resultado
#image("image-3.png")


=== Comprensión de la espiral de Arquímedes en un compresor scroll

En el compresor scroll, estas espirales dobles crean cámaras de compresión cuyo volumen disminuye a medida que las espirales se mueven relativamente entre sí. El gas queda atrapado en estas cámaras y se comprime conforme es forzado hacia el centro.

=== Conclusión

La generación de las espirales de Arquímedes utilizando Google Colab demuestra la potencia y accesibilidad de esta herramienta para visualizaciones matemáticas. La plataforma permite implementar fácilmente las ecuaciones polares y crear representaciones visuales precisas que ayudan a comprender mejor el funcionamiento de los compresores scroll.

=== Captura de pantalla del código ejecutado
#image("image-4.png")