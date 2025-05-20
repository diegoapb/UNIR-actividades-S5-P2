#import "@preview/charged-ieee:0.1.3": ieee

#show: ieee.with(
  title: [Trabajo: Cargas, campo y fuerza electrostática],
  abstract: [
    Este documento aborda ejercicios de electromagnetismo sobre cargas, campos y fuerzas electrostáticas. Se analiza la trayectoria de un electrón en un campo magnético, calculando su radio, frecuencia y período orbital, y se compara con un antineutrón. También se calcula la fuerza magnética sobre un electrón solar entrando en la aurora de Júpiter. Finalmente, se determina la magnitud y dirección de un campo eléctrico en equilibrio con una gota de aceite, similar al experimento de Millikan. Cada ejercicio requiere desarrollo matemático y justificación de supuestos.
  ],
  authors: (
    (
      name: "Diego Alejandro Parra Bravo",
      department: [Fisica II],
      organization: [Universidad Internacional de La Rioja],
      location: [Cali, Colombia],
      email: "dap465@gmail.coom"
    ),
  ),
  // index-terms: ("Scientific writing", "Typesetting", "Document creation", "Syntax"),
  bibliography: bibliography("refs.bib"),
  // figure-supplement: [Fig.],
)

= Primer ejercicio <sec:primer-ejercicio>

Un electrón con una capacidad de trabajo de $72090 times 10^(-19) space "J"$ orbita de manera perpendicular a un campo magnético de $3250 space "G"$. ¿Cuál es el radio de la órbita? ¿Y su frecuencia y periodo angular? Resuelve el mismo ejercicio para un antineutrón.

== Solución

=== Datos proporcionados y constantes
- Energía cinética ($E$): $72090 times 10^(-19) space "J" = 7.209 times 10^(-15) space "J"$
- Campo magnético ($B$): $3250 space "G" = 3250 times 10^(-4) space "T" = 0.325 space "T"$
- Carga del electrón ($C_e$): $-1.602 times 10^(-19) space "C"$.
- Masa del electrón ($m_e$): $9.109 times 10^(-31) space "kg"$
- Masa del antineutrón ($m_(\b{n})$): $1.6749 times 10^(-27) space "kg"$ (aproximadamente igual a la masa del neutrón)
- Carga del antineutrón ($q_(\b{n})$): $0 space "C"$

=== Parte A: Electrón

La "capacidad de trabajo" se interpreta como la energía cinética ($E$) del electrón. La energía cinética se relaciona con la velocidad ($v$) mediante la fórmula:
$ E = 1/2 m_e v^2 $
Despejando la velocidad $v$:
$ v = sqrt((2 E) / m_e) $
Sustituyendo los valores:
$ v = sqrt((2 times 7.209 times 10^(-15) space "J") / (9.109 times 10^(-31) space "kg")) $
$ v = sqrt((1.4418 times 10^(-14) space "J") / (9.109 times 10^(-31) space "kg")) $
$ v = sqrt(1.58283 times 10^(16) space "m"^2"/s"^2) approx 1.2581 times 10^8 space "m/s" $

Cuando una partícula cargada se mueve perpendicularmente a un campo magnético, la fuerza magnética ($F_B$) actúa como fuerza centrípeta ($F_c$), causando un movimiento circular.
$ F_B = |C_e| v B $
$ F_c = (m_e v^2) / r $
Igualando ambas fuerzas $F_B = F_c$:
$ |C_e| v B = (m_e v^2) / r $
Despejando el radio $r$:
$ r = (m_e v) / (|C_e| B) $
Sustituyendo los valores:
$ r = ((9.109 times 10^(-31) space "kg") times (1.2581 times 10^8 space "m/s")) / ((1.602 times 10^(-19) space "C") times (0.325 space "T")) $
$ r = (1.1460 times 10^(-22) space "kg m/s") / (0.52065 times 10^(-19) space "C T") $
$ r approx 2.1999 times 10^(-3) space "m" = 2.20 space "mm" $

La frecuencia de ciclotrón ($f$) es la frecuencia del movimiento orbital y está dada por:
$ f = (|C_e| B) / (2 pi m_e) $
Sustituyendo los valores:
$ f = ((1.602 times 10^(-19) space "C") times (0.325 space "T")) / (2 pi times (9.109 times 10^(-31) space "kg")) $
$ f = (0.52065 times 10^(-19) space "C T") / (5.7234 times 10^(-30) space "kg") $
$ f approx 9.097 times 10^9 space "Hz" = 9.097 space "GHz" $

El período angular ($T$), o simplemente período, es el inverso de la frecuencia:
$ T = 1 / f $
Sustituyendo el valor de $f$:
$ T = 1 / (9.097 times 10^9 space "Hz") approx 1.099 times 10^(-10) space "s" = 0.110 space "ns" $

*Resultados para el electrón:*
- Radio de la órbita ($r$): $2.20 space "mm"$
- Frecuencia ($f$): $9.097 space "GHz"$
- Período angular ($T$): $0.110 space "ns"$

=== Parte B: Antineutrón

Un c es la antipartícula del neutrón. Posee la misma masa que el neutrón, $m_(\b{n}) approx 1.6749 times 10^(-27) space "kg"$, pero, de manera crucial para este problema, tiene una carga eléctrica neta de $q_(\b{n}) = 0 space "C"$.

*Resultados para el antineutrón:*
- Radio de la órbita ($r$): No aplica (o se considera infinito), ya que no hay órbita.
- Frecuencia ($f$): $0 space "Hz"$, al no haber movimiento periódico orbital.
- Período angular ($T$): No aplica (o se considera infinito).

= Segundo ejercicio <sec:segundo-ejercicio>

Calcula el módulo de la fuerza magnética que actúa sobre un electrón proveniente del Sol que penetra en la aurora boreal joviana. Haz cálculos aproximados basados en la búsqueda de información relativa a Júpiter, su campo magnético y el fundamento físico de una aurora boreal. Asume que la velocidad del electrón es prácticamente la de la luz. (Información adicional: Campo magnético de Júpiter $approx 14$ veces el de la Tierra; Campo magnético promedio de la Tierra $approx 0.5 space "G"$.

== Solución

=== Datos proporcionados, constantes y suposiciones
- Carga del electrón ($|q_e|$): $1.602 times 10^(-19) space "C"$
- Velocidad del electrón ($v$): Se asume prácticamente la velocidad de la luz, $c approx 3.00 times 10^8 space "m/s"$.
- Campo magnético promedio de la Tierra ($B_T$): $0.5 space "G" = 0.5 times 10^(-4) space "T"$.
- Campo magnético de Júpiter ($B_J$): $14 times B_T$.
- Conversión: $1 space "G" = 10^(-4) space "Tesla (T)"$.
- Ángulo de incidencia: Para un cálculo aproximado del módulo de la fuerza, se considerará que el electrón penetra el campo magnético de Júpiter de tal manera que su velocidad tiene una componente significativa perpendicular al campo. Para estimar la magnitud de la fuerza, podemos asumir que el ángulo $theta$ entre la velocidad $v$ y el campo magnético $B$ es $90^o$, por lo que $sin(theta) = 1$. Esto nos dará la fuerza máxima posible.

=== Cálculo del campo magnético de Júpiter
Primero, calculamos el campo magnético de Júpiter en Tesla:
$ B_J = 14 times B_T = 14 times (0.5 space "G") = 7 space "G" $
Convirtiendo a Tesla:
$ B_J = 7 space "G" times (10^(-4) space "T/G") = 7 times 10^(-4) space "T" $

=== Cálculo de la Fuerza Magnética
La magnitud de la fuerza magnética ($F_B$) sobre una partícula cargada está dada por la Ley de Lorentz:
$ F_B = |q_e| v B_J sin(theta) $
Con nuestra suposición de $sin(theta) = 1$:
$ F_B = |q_e| v B_J $
Sustituyendo los valores:
$ F_B = (1.602 times 10^(-19) space "C") times (3.00 times 10^8 space "m/s") times (7 times 10^(-4) space "T") $
$ F_B = (1.602 times 3.00 times 7) times (10^(-19) times 10^8 times 10^(-4)) space "N" $
$ F_B = 33.642 times 10^(-19 + 8 - 4) space "N" $
$ F_B = 33.642 times 10^(-15) space "N" $
$ F_B approx 3.36 times 10^(-14) space "N" $

*Resultado para la fuerza magnética sobre el electrón:*
- Módulo de la fuerza magnética ($F_B$): Aproximadamente $3.36 times 10^(-14) space "N"$.

*Conclusión*
La fuerza magnética que actúa sobre un electrón proveniente del Sol al penetrar en la aurora boreal joviana es aproximadamente $3.36 times 10^(-14) space "N"$. Este valor es significativo y muestra la interacción entre el electrón y el campo magnético de Júpiter, lo que contribuye a la dinámica de la aurora boreal en ese planeta.

= Tercer ejercicio <sec:tercer-ejercicio>

Se tiene una cantidad pequeña de material lubricante de masa $2.41 times 10^(10) space "u"$ (unidades de masa atómica) y una carga de $4.8 times 10^(-19) space "C"$. La gota de aceite se encuentra flotando en equilibrio gracias a la harmonía de la fuerza gravitatoria más otra fuerza extra de naturaleza eléctrica. ¿Cuál es la dirección y magnitud del campo eléctrico originado por dicha fuerza? ¿A qué te recuerda la experiencia descrita? Justifica tu respuesta.

== Solución

=== Datos proporcionados y constantes
- Masa de la gota de aceite ($m_u$): $2.41 times 10^(10) space "u"$
- Carga de la gota de aceite ($q$): $4.8 times 10^(-19) space "C"$ (positiva)
- Unidad de masa atómica ($1 space "u"$): $1.66054 times 10^(-27) space "kg"$
- Aceleración debida a la gravedad ($g$): $9.81 space "m/s"^2$

=== Conversión de la masa a kilogramos
Primero, convertimos la masa de la gota de aceite de unidades de masa atómica (u) a kilogramos (kg):
$ m = m_u times (1.66054 times 10^(-27) space "kg/u") $
$ m = (2.41 times 10^(10) space "u") times (1.66054 times 10^(-27) space "kg/u") $
$ m = (2.41 times 1.66054) times (10^(10) times 10^(-27)) space "kg" $
$ m = 4.0019014 times 10^(-17) space "kg" $
$ m approx 4.00 times 10^(-17) space "kg" $

=== Análisis de las fuerzas y condición de equilibrio
La gota de aceite está flotando en equilibrio. Esto significa que la suma de las fuerzas que actúan sobre ella es cero. Las fuerzas involucradas son:
1.  *Fuerza gravitatoria* ($F_g$): Actúa hacia abajo y su magnitud es $F_g = m g$.
2.  *Fuerza eléctrica* ($F_e$): Para que la gota esté en equilibrio, esta fuerza debe actuar hacia arriba y tener una magnitud igual a la fuerza gravitatoria. Su magnitud es $F_e = |q| E$, donde $|q|$ es el valor absoluto de la carga eléctrica y $E$ es la magnitud del campo eléctrico.

En equilibrio:
$ F_e = F_g $
$ |q| E = m g $

=== Cálculo de la magnitud del campo eléctrico ($E$)
Despejamos $E$ de la ecuación de equilibrio:
$ E = (m g) /(|q|) $
Sustituyendo los valores:
$ E = ((4.00 times 10^(-17) space "kg") times (9.81 space "m/s"^2)) / (4.8 times 10^(-19) space "C") $
$ E = (3.924 times 10^(-16) space "N") / (4.8 times 10^(-19) space `"C") $
$ E = (3.924 / 4.8) times (10^(-16) / 10^(-19)) space "N/C" $
$ E = 0.8175 times 10^3 space "N/C" $
$ E = 817.5 space "N/C" $

La magnitud del campo eléctrico es aproximadamente $817.5 space "N/C"$. donde N es Newton y C es Coulomb.

=== Dirección del campo eléctrico
La fuerza gravitatoria ($vec(F)_g$) actúa hacia abajo. Para que la gota esté en equilibrio, la fuerza eléctrica ($vec(F)_e$) debe actuar hacia arriba.
La relación entre la fuerza eléctrica y el campo eléctrico es $vec(F)_e = q vec(E)$.
Dado que la carga $q = 4.8 times 10^(-19) space "C"$ es positiva, la dirección del campo eléctrico $vec(E)$ debe ser la misma que la dirección de la fuerza eléctrica $vec(F)_e$.
Por lo tanto, el campo eléctrico está dirigido *hacia arriba*.

=== Experiencia similar
Esta experiencia es una analogía directa del *experimento de la gota de aceite de Millikan* @tipler2008.

*Justificación:*
El experimento de Millikan, realizado por Robert A. Millikan y Harvey Fletcher en 1909, tenía como objetivo medir la carga elemental del electrón ($e$). En su experimento, pequeñas gotas de aceite cargadas eléctricamente eran suspendidas en un campo eléctrico vertical ajustado de tal manera que la fuerza eléctrica hacia arriba equilibrara exactamente la fuerza gravitatoria hacia abajo @tipler2008.
Al medir la masa de la gota y el campo eléctrico necesario para suspenderla, Millikan pudo determinar la carga de la gota. Observó que las cargas eran siempre múltiplos enteros de un valor fundamental, que identificó como la carga del electrón.

El escenario descrito en el problema —una gota de aceite cargada suspendida en equilibrio por un campo eléctrico que contrarresta la gravedad— es precisamente la configuración central del experimento de Millikan.

*Resultados para el tercer ejercicio:*
- Magnitud del campo eléctrico ($E$): $817.5 space "N/C"$
- Dirección del campo eléctrico: Hacia arriba.
- Experiencia similar: Experimento de la gota de aceite de Millikan.