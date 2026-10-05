# Retroalimentación — Laboratorio evaluativo 01: Fundamentos, complejidad y recurrencias

**Estudiante:** Santiago Martínez Gutiérrez · **Laboratorio:** Plataforma Tamiza, ordenamiento y recurrencias
**Fecha límite:** 2026-10-04 23:59 · **Versión revisada:** commit `e05683e`

Muy buen trabajo: el informe está completo, ordenado y apoyado en sus propias mediciones.

## Nota

| Criterio | Puntos |
|---|---|
| Corrección conceptual | 22 / 25 |
| Calidad de la explicación teórica | 21 / 25 |
| Corrección de la implementación | 15 / 20 |
| Calidad del análisis de las gráficas | 15 / 20 |
| Documentación y organización del informe | 9 / 10 |
| **Total** | **82 / 100** |
| **Nota (0–5)** | **4.10** |

## 1. Corrección conceptual (22 / 25)
**Lo que hizo bien:**
- Distingue bien entre que el algoritmo sea correcto y que sea eficiente, y nombra la restricción que se incumple: la ventana de 4 horas.
- Explica con claridad por qué duplicar la velocidad del servidor no arregla el problema (el costo crece con n²).
- El ejemplo propio (revisión de plagio entre 300 trabajos) es concreto, con cantidades y restricción.
- En la Parte 2 identifica dos perjuicios (el paciente y la Secretaría) y explica por qué el orden de la lista exige exactitud.

**Lo que puede mejorar:**
- En la parte ambiental falta pasar de "media hora de más" a una cifra aproximada de energía o de horas acumuladas al año.
- El segundo perjuicio (gasto de la Secretaría) es más económico que humano; faltó una segunda persona afectada, por ejemplo el operador del centro de contacto.
- Cuide el tono: expresiones como "no sé" suenan poco profesionales en un informe.

## 2. Calidad de la explicación teórica (21 / 25)
**Lo que hizo bien:**
- Define los tres casos indicando sobre qué se toma el máximo, el mínimo y el promedio, y justifica usar el peor caso.
- La predicción quedó escrita antes del experimento.
- La recurrencia de merge sort está bien explicada y resuelta paso a paso, con costo por nivel y número de niveles.
- El análisis línea a línea de insertion sort y la tabla de complejidades están completos.

**Lo que puede mejorar:**
- El árbol de recursión está descrito con palabras, pero no dibujado (en imagen o en texto dentro de un bloque de código).
- En la tabla de insertion sort, el costo de la línea del `while` y de los corrimientos podría detallarse mejor al sumar el total.

## 3. Corrección de la implementación (15 / 20)
**Lo que hizo bien:**
- `insertion_sort` y `merge_sort` ordenan bien, no cambian la lista recibida, cuentan solo comparaciones entre elementos y no usan `sorted()` ni `sort()`. La mezcla de merge sort es propia.
- Los tres generadores producen valores distintos, del tamaño pedido y con semilla reproducible.
- No hay problemas de estilo (PEP 8) y las funciones principales llevan sus tipos.

**Lo que puede mejorar:**
- Los tres generadores de `datos.py` tienen un docstring de una sola línea; faltan las secciones `Args` y `Returns` del estilo Google.
- En `parte3_casos.py` y `parte4_complejidad.py` varias funciones (`graficar_comparaciones`, `graficar_tiempo`, `main`, `medir` en la Parte 4) no tienen docstring completo ni todas llevan tipos.

## 4. Calidad del análisis de las gráficas (15 / 20)
**Lo que hizo bien:**
- Las tres gráficas existen, con título, ejes, unidades y leyenda, y están bien incrustadas.
- Identifica con datos el peor caso (C) y el mejor (B), y contrasta con su predicción; el dato de 19.900 comparaciones con n=200 es una buena comprobación.
- En la Parte 4 describe lo que hace cada curva y lo conecta con lo calculado.
- La estimación de insertion sort para 1.200.000 registros (unas 5,2 horas) está bien razonada y declarada como estimación.

**Lo que puede mejorar:**
- No dice explícitamente cuál escenario se aproxima al caso promedio (era el A).
- Para merge sort solo dice "del orden de segundos": falta hacer la cuenta con n log n y dar un número.
- Al responder sobre el servidor, cite la gráfica concreta de donde sale el dato.
- En la gráfica de comparaciones, la curva del escenario B queda pegada al eje; una escala logarítmica la haría visible.

## 5. Documentación y organización del informe (9 / 10)
**Lo que hizo bien:**
- Siguió la estructura de carpetas acordada y tiene los archivos y gráficas pedidos.
- Cada parte práctica enlaza su código, hay instrucciones para reproducir y 7 commits descriptivos.

**Lo que puede mejorar:**
- Escriba su nombre completo (nombres y apellidos) al inicio del informe.

## ¿El código funciona?
Sí. Los dos scripts corren sin errores, ordenan correctamente y generan las tres gráficas.

## Para el próximo laboratorio
- Complete los docstrings (con `Args` y `Returns`) y los tipos en todas las funciones, incluidas las auxiliares.
- Dibuje los árboles de recursión en un bloque de texto o como imagen.
- Al extrapolar, calcule también el número para el algoritmo recomendado.
- Cuantifique el impacto ambiental con cifras aproximadas.
- Mantenga un tono profesional y revise que cada pregunta quede respondida de forma explícita.
