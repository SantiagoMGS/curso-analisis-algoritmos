"""Validacion experimental de la parte 4: insertion sort vs merge sort.

Mide el tiempo de los dos algoritmos sobre el escenario A (aleatorio),
que es el mas realista para lo que le puede llegar a Tamiza por el
portal web de los laboratorios.
"""

import pathlib
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort, merge_sort
from datos import generar_aleatorio

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3


def medir(funcion, n: int) -> float:
    tiempos = []
    for _ in range(REPETICIONES):
        datos = generar_aleatorio(n)
        inicio = time.perf_counter()
        funcion(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.mean(tiempos)


def main() -> None:
    tiempos_insertion = []
    tiempos_merge = []

    for n in TAMANOS:
        t_insertion = medir(insertion_sort, n)
        t_merge = medir(merge_sort, n)
        tiempos_insertion.append(t_insertion)
        tiempos_merge.append(t_merge)
        print(f"n={n}: insertion_sort={t_insertion:.6f} s, merge_sort={t_merge:.6f} s")

    plt.figure()
    plt.plot(TAMANOS, tiempos_insertion, marker="o", label="insertion sort")
    plt.plot(TAMANOS, tiempos_merge, marker="o", label="merge sort")
    plt.title("Tiempo de ejecucion vs tamano del lote (escenario A)")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte4_tiempo.png")
    plt.close()


if __name__ == "__main__":
    main()
