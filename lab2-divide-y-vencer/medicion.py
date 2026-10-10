"""Medicion de tiempos: fuerza bruta contra divide y venceras."""

import pathlib
import random
import statistics
import time

import matplotlib.pyplot as plt

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo

CARPETA = pathlib.Path(__file__).resolve().parent
TAMANOS = [10, 50, 100, 500, 1000, 2000, 4000, 8000]
REPETICIONES = 3
SEMILLA = 2026


def generar_serie(n: int) -> list[int]:
    """Genera n variaciones diarias enteras entre -100 y 100."""
    rng = random.Random(SEMILLA + n)
    return [rng.randint(-100, 100) for _ in range(n)]


def medir(funcion, *args) -> float:
    """Devuelve la mediana de varias corridas de la funcion, en segundos."""
    tiempos = []
    for _ in range(REPETICIONES):
        inicio = time.perf_counter()
        funcion(*args)
        tiempos.append(time.perf_counter() - inicio)
    return statistics.median(tiempos)


def main() -> None:
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
