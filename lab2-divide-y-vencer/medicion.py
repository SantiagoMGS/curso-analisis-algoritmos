"""Medicion de tiempos: fuerza bruta contra divide y venceras."""

import pathlib
import random
import statistics
import time
from collections.abc import Callable
from typing import Any

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 2026


def generar_serie(n: int) -> list[int]:
    """Genera n variaciones diarias enteras entre -100 y 100.

    Args:
        n: cantidad de dias de la serie.

    Returns:
        Lista de n enteros; la semilla depende de n, asi que la misma
        llamada siempre devuelve la misma serie.
    """
    rng = random.Random(SEMILLA + n)
    return [rng.randint(-100, 100) for _ in range(n)]


def medir(funcion: Callable[..., Any], *args: Any) -> float:
    """Mide una funcion varias veces y devuelve la mediana de los tiempos.

    Args:
        funcion: funcion a cronometrar.
        *args: argumentos con los que se llama a la funcion.

    Returns:
        Mediana del tiempo de ejecucion, en segundos.
    """
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion(*args)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
    """Mide ambos algoritmos en todos los tamanos y guarda la grafica."""
    tiempos_fb = []
    tiempos_dc = []

    for n in TAMANOS:
        serie = generar_serie(n)

        suma_fb = subarreglo_fuerza_bruta(serie)[2]
        suma_dc = subarreglo_maximo(serie, 0, n - 1)[2]
        assert suma_fb == suma_dc, f"las sumas no coinciden para n={n}"

        t_fb = medir(subarreglo_fuerza_bruta, serie)
        t_dc = medir(subarreglo_maximo, serie, 0, n - 1)
        tiempos_fb.append(t_fb)
        tiempos_dc.append(t_dc)
        print(f"n={n}: fuerza bruta={t_fb:.6f} s, divide y venceras={t_dc:.6f} s")

    plt.figure()
    plt.plot(TAMANOS, tiempos_fb, marker="o", label="Fuerza bruta")
    plt.plot(TAMANOS, tiempos_dc, marker="o", label="Divide y venceras")
    plt.title("Subarreglo maximo: tiempo de ejecucion vs tamano de la serie")
    plt.xlabel("Tamano de la serie (n, dias)")
    plt.ylabel("Tiempo de ejecucion (segundos)")
    plt.legend()
    plt.savefig(CARPETA / "graficas" / "tiempo_vs_n.png")
    plt.close()


if __name__ == "__main__":
    main()
