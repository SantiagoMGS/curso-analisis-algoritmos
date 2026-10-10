# Laboratorio evaluativo 2 — Dividir y vencer

**Nombre:** Santiago Martínez

## Cómo reproducir

Desde la raíz del repositorio, con el entorno virtual activado:

```bash
source venv/Scripts/activate      # en Linux/Mac: source venv/bin/activate
pip install -r requirements.txt
cd lab2-divide-y-vencer
python pruebas.py                 # imprime "Todas las pruebas pasaron" si todo está bien
python medicion.py                # imprime los tiempos y genera graficas/tiempo_vs_n.png
```

---

## Parte 1 — Implementar y verificar

Código: [`subarreglo.py`](subarreglo.py) (las tres funciones) y [`pruebas.py`](pruebas.py) (las verificaciones).

Las pruebas son `assert` y comparan la **suma** de cada resultado, no los índices, porque puede haber varios tramos con la misma suma máxima. Los casos que cubren son:

- La serie de ocho días de la situación problema (`[-3, 5, -2, 8, -6, 3, 9, -4]`), que debe dar 17 en las dos funciones.
- Una serie de un solo elemento (uno positivo y uno negativo).
- Una serie con todos los valores negativos, donde el resultado es el menos negativo.
- Una serie con todos los valores positivos, donde el tramo es la serie completa.
- Un caso donde el mejor tramo cruza el punto medio (`[-5, -5, -5, 6, 7, -5, -5, -5]`, tramo de los índices 3 a 4 con suma 13), para comprobar que `suma_cruzada` está bien.
- Que ninguna de las dos funciones modifica la lista que recibe.
- 50 listas aleatorias de entre 1 y 60 elementos (semilla fija) en las que la fuerza bruta y el divide y vencerás tienen que dar la misma suma.

---

## Parte 2 — Medir y graficar

Código: [`medicion.py`](medicion.py).

Medí ocho tamaños: 10, 50, 100, 500, 1000, 2000, 4000 y 8000. Los datos son enteros entre -100 y 100 generados con semilla fija, y para cada tamaño las dos funciones reciben la misma lista. Antes de medir, el script comprueba que ambas dan la misma suma. Cada medición se repitió tres veces con `time.perf_counter()` (solo se cronometra la llamada al algoritmo, no la generación de datos) y se grafica la mediana.

![Tiempo de ejecución contra tamaño de la serie](graficas/tiempo_vs_n.png)

Valores medidos (mediana de 3 corridas):

| n | Fuerza bruta (s) | Divide y vencerás (s) |
|---|---|---|
| 10 | 0,000003 | 0,000006 |
| 50 | 0,000032 | 0,000027 |
| 100 | 0,000121 | 0,000057 |
| 500 | 0,003419 | 0,000329 |
| 1000 | 0,013944 | 0,000734 |
| 2000 | 0,062012 | 0,001525 |
| 4000 | 0,232381 | 0,002992 |
| 8000 | 0,917274 | 0,006343 |
