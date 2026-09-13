"""Algoritmos de ordenamiento instrumentados para el Laboratorio 1.

Ambos algoritmos ordenan de mayor a menor indice de riesgo (el orden
que necesita Tamiza para priorizar las llamadas) y cuentan unicamente
las comparaciones entre elementos de la lista.
"""


def insertion_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de insercion.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    resultado = list(datos)
    comparaciones = 0

    for i in range(1, len(resultado)):
        actual = resultado[i]
        j = i - 1
        while j >= 0:
            comparaciones += 1
            if resultado[j] < actual:
                resultado[j + 1] = resultado[j]
                j -= 1
            else:
                break
        resultado[j + 1] = actual

    return resultado, comparaciones
