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


def merge_sort(datos: list[int]) -> tuple[list[int], int]:
    """Ordena una lista de indices de riesgo con el metodo de mezcla.

    No modifica la lista recibida: trabaja sobre una copia.

    Args:
        datos: lista de indices de riesgo a ordenar.

    Returns:
        Una tupla con la lista ordenada y el numero total de
        comparaciones entre elementos realizadas durante el proceso.
    """
    if len(datos) <= 1:
        return list(datos), 0

    medio = len(datos) // 2
    izquierda, comparaciones_izq = merge_sort(datos[:medio])
    derecha, comparaciones_der = merge_sort(datos[medio:])
    mezclado, comparaciones_mezcla = _mezclar(izquierda, derecha)

    return mezclado, comparaciones_izq + comparaciones_der + comparaciones_mezcla


def _mezclar(izquierda: list[int], derecha: list[int]) -> tuple[list[int], int]:
    """Combina dos listas ya ordenadas de mayor a menor en una sola."""
    resultado = []
    comparaciones = 0
    i = j = 0

    while i < len(izquierda) and j < len(derecha):
        comparaciones += 1
        if izquierda[i] >= derecha[j]:
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])
    return resultado, comparaciones
