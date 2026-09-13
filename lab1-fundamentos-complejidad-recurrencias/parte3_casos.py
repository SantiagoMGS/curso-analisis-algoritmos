"""Experimento de la parte 3: peor, mejor y caso promedio de insertion sort.

Predije antes de correr esto que el escenario C (orden inverso) iba a ser
el peor caso porque es exactamente el orden contrario al que arma
insertion_sort, y que B (casi ordenado) iba a ser el mejor porque casi no
hay que mover nada. El experimento de abajo lo confirma o lo desmiente
segun los numeros que salgan.
"""

import pathlib
import statistics
import time

import matplotlib.pyplot as plt

from algoritmos import insertion_sort
from datos import generar_aleatorio, generar_casi_ordenado, generar_inverso

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [100, 200, 400, 800, 1600, 3200, 6400]
REPETICIONES = 3

ESCENARIOS = {
    "A - aleatorio": generar_aleatorio,
    "B - casi ordenado": generar_casi_ordenado,
    "C - orden inverso": generar_inverso,
}


def medir(generador, n: int) -> tuple[float, int]:
    """Corre insertion_sort varias veces sobre un lote de tamano n y
    devuelve el tiempo promedio y el numero de comparaciones (que no
    cambia entre repeticiones porque los datos son siempre los mismos).
    """
    tiempos = []
    comparaciones = 0
    for _ in range(REPETICIONES):
        datos = generador(n)
        inicio = time.perf_counter()
        _, comparaciones = insertion_sort(datos)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.mean(tiempos), comparaciones


def graficar_comparaciones(resultados: dict) -> None:
    plt.figure()
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores["comparaciones"], marker="o", label=nombre)
    plt.title("Insertion sort: comparaciones segun el escenario de entrada")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Numero de comparaciones")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte3_comparaciones.png")
    plt.close()


def graficar_tiempo(resultados: dict) -> None:
    plt.figure()
    for nombre, valores in resultados.items():
        plt.plot(TAMANOS, valores["tiempos"], marker="o", label=nombre)
    plt.title("Insertion sort: tiempo de ejecucion segun el escenario de entrada")
    plt.xlabel("Tamano del lote (n)")
    plt.ylabel("Tiempo (segundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "parte3_tiempo.png")
    plt.close()


def main() -> None:
    resultados = {nombre: {"tiempos": [], "comparaciones": []} for nombre in ESCENARIOS}

    for nombre, generador in ESCENARIOS.items():
        for n in TAMANOS:
            tiempo, comparaciones = medir(generador, n)
            resultados[nombre]["tiempos"].append(tiempo)
            resultados[nombre]["comparaciones"].append(comparaciones)
            print(f"{nombre}, n={n}: {comparaciones} comparaciones, {tiempo:.6f} s")

    graficar_comparaciones(resultados)
    graficar_tiempo(resultados)


if __name__ == "__main__":
    main()
