"""Generadores de lotes de registros para los escenarios de Tamiza.

Los tres generadores producen listas de n valores unicos (sin empates
en el indice de riesgo) para que el orden resultante sea el mismo sin
importar el algoritmo usado.
"""

import random


def generar_aleatorio(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote de n registros en orden aleatorio (escenario A)."""
    rng = random.Random(semilla)
    valores = list(range(1, n + 1))
    rng.shuffle(valores)
    return valores


def generar_casi_ordenado(n: int, semilla: int = 42) -> list[int]:
    """Genera un lote casi ordenado: 98% ordenado y 2% al final (escenario B)."""
    rng = random.Random(semilla)
    # descendente porque es el orden que Tamiza necesita (mayor riesgo primero)
    valores = list(range(n, 0, -1))
    cantidad_desordenada = max(1, round(n * 0.02))
    cola = valores[-cantidad_desordenada:]
    rng.shuffle(cola)
    return valores[:-cantidad_desordenada] + cola


def generar_inverso(n: int) -> list[int]:
    """Genera un lote en el orden exactamente contrario (escenario C)."""
    # ascendente: al reves del orden descendente que necesita Tamiza
    return list(range(1, n + 1))
