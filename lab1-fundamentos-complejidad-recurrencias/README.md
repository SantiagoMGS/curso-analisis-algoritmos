# Laboratorio evaluativo 1 — Fundamentos, complejidad y recurrencias

**Nombre:** Santiago Martínez

## Cómo reproducir el experimento

Desde la raíz del repositorio, con el entorno virtual ya creado según el Laboratorio 2:

```bash
source venv/Scripts/activate      # o venv/bin/activate en Linux/Mac
pip install -r requirements.txt
cd lab1-fundamentos-complejidad-recurrencias
python parte3_casos.py            # genera graficas/parte3_comparaciones.png y parte3_tiempo.png
python parte4_complejidad.py      # genera graficas/parte4_tiempo.png
```

Cada script imprime en consola los mismos números que se usan en las secciones de abajo, por si se quiere comparar sin volver a correrlo.

---

## Parte 1 — Analizar el algoritmo antes de comprar hardware

Que el proceso de Tamiza lleve ocho años entregando el resultado correcto no dice nada sobre si es un buen algoritmo, dice que **es correcto**: dado cualquier lote de 1.200.000 registros, insertion sort termina y entrega la lista ordenada. Eso no está en discusión. El problema es otro: **eficiencia**, es decir, cuántos recursos (en este caso, tiempo) necesita para terminar. Y la restricción concreta que se está incumpliendo es la ventana de 4 horas: el proceso puede ser perfectamente correcto y aun así no caber en el tiempo disponible, porque corrección y eficiencia son dos preguntas distintas. Un algoritmo puede tardar una hora o puede tardar un año y en ambos casos entregar la respuesta correcta.

Duplicar la velocidad del servidor no resuelve esto porque insertion sort tiene un costo que crece proporcional a n², no a n. Si el número de registros se duplicó al ampliar el programa a todo el departamento, el tiempo de ordenamiento no se duplicó: se multiplicó por cuatro (porque (2n)² = 4n²). Comprar un servidor el doble de rápido solo divide ese tiempo entre dos, así que en la práctica el proceso vuelve a quedar donde estaba antes de la ampliación, o peor, porque la cantidad de registros va a seguir creciendo y cada vez que se duplique otra vez el volumen, va a hacer falta duplicar la velocidad del hardware otra vez. Es una solución que hay que repetir cada pocos meses, mientras que cambiar el algoritmo por uno de complejidad n log n resuelve el problema de fondo una sola vez, sin importar cuánto crezca el departamento después.

Un ejemplo distinto: una universidad que revisa el plagio de los trabajos finales comparando cada entrega contra todas las demás entregas del mismo curso. Si un curso tiene 300 estudiantes, comparar cada trabajo contra los otros 299 significa del orden de 300×299 comparaciones de texto, y ese número también crece cuadráticamente si el curso crece a 600 estudiantes (ahí serían cuatro veces más comparaciones, no el doble). La universidad podría comprar un servidor más rápido para que las comparaciones de texto se hagan más rápido, pero si en unos años los cursos masivos llegan a 3000 estudiantes, el número de comparaciones no se sostiene con hardware: hay que cambiar el método (por ejemplo, usando huellas digitales de texto en vez de comparar todo contra todo) porque la restricción que se incumple no es "el procesador es lento", es que el algoritmo hace más trabajo del que el sistema puede pagar a esa escala.

---

## Parte 2 — Responsabilidad ambiental y ética

**Dimensión ambiental.** Cada minuto que el proceso de Tamiza tarda de más es CPU encendida consumiendo energía, y esto no es un gasto de una sola vez: el proceso corre todas las madrugadas, los 365 días del año, durante los años que la plataforma siga en producción (lleva 8 y nada indica que vaya a cambiar pronto). Si insertion sort tarda, por decir un número, media hora más que un algoritmo n log n en el mismo hardware, esa media hora se repite unas 365 veces al año, y otra vez el año siguiente. Elegir mal el algoritmo no es un costo ambiental puntual, es una decisión que se paga en electricidad (y en las emisiones asociadas a generarla) cada noche, indefinidamente, hasta que alguien decida corregirla.

**Dimensión ética.** Acá hay al menos dos formas concretas en que decidir mal el algoritmo perjudica a alguien identificable:

1. Si el proceso no termina dentro de la ventana de 4 horas, la lista de llamadas del día queda incompleta —de hecho ya pasó 3 veces— y eso significa que hay pacientes con riesgo cardiovascular alto que no reciben la llamada de seguimiento ese día. El costo lo asume directamente **el paciente**, que puede ser alguien que necesitaba esa llamada para ajustar un tratamiento a tiempo.
2. Si la respuesta ante el desbordamiento es "compremos un servidor más rápido" en vez de corregir el algoritmo, el costo económico recurrente (cada vez que el volumen vuelva a crecer, tocará comprar hardware otra vez) lo termina asumiendo **la Secretaría de Salud**, que paga infraestructura de más para tapar un problema que es de diseño de software, dinero que podría ir a ampliar la cobertura del programa en vez de a servidores.

Además, el orden en que queda la lista no es un detalle técnico: decide literalmente a quién se llama primero. Si el ordenamiento tiene un error o no logra terminar completo, no es que "algunos pacientes" se atrasen al azar, es que el sistema está tomando —sin que nadie lo decida explícitamente— quién queda de primero y quién de último en una lista de prioridad de riesgo cardiovascular. Eso le pone al ordenamiento una exigencia adicional que no tendría si solo estuviera ordenando, no sé, nombres de productos en un catálogo: no basta con que "generalmente" quede bien ordenado, tiene que ser exacto, porque un error de ordenamiento acá se traduce directo en que alguien de mayor riesgo quede más abajo en la lista que alguien de menor riesgo.

---
