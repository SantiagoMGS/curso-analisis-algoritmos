"""Pruebas de las dos soluciones del subarreglo maximo."""

import random

from subarreglo import subarreglo_fuerza_bruta, subarreglo_maximo


def suma_dc(valores: list[float]) -> float:
    return subarreglo_maximo(valores, 0, len(valores) - 1)[2]


# serie de la situacion problema
serie = [-3, 5, -2, 8, -6, 3, 9, -4]
assert subarreglo_fuerza_bruta(serie)[2] == 17
assert suma_dc(serie) == 17

# un solo elemento
assert subarreglo_fuerza_bruta([7])[2] == 7
assert suma_dc([7]) == 7
assert subarreglo_fuerza_bruta([-4])[2] == -4
assert suma_dc([-4]) == -4

# todos negativos: gana el menos negativo
negativos = [-8, -3, -6, -2, -9]
assert subarreglo_fuerza_bruta(negativos)[2] == -2
assert suma_dc(negativos) == -2

# todos positivos: gana la serie completa
positivos = [4, 1, 7, 3, 5]
assert subarreglo_fuerza_bruta(positivos) == (0, 4, 20)
assert subarreglo_maximo(positivos, 0, 4) == (0, 4, 20)

# el mejor tramo cruza el punto medio (indices 3 y 4 en una lista de 8)
cruzado = [-5, -5, -5, 6, 7, -5, -5, -5]
assert subarreglo_fuerza_bruta(cruzado) == (3, 4, 13)
assert subarreglo_maximo(cruzado, 0, 7) == (3, 4, 13)

# la lista recibida no se modifica
copia = list(serie)
subarreglo_fuerza_bruta(serie)
subarreglo_maximo(serie, 0, len(serie) - 1)
assert serie == copia

# listas aleatorias de distintos tamanos: las dos deben coincidir en la suma
random.seed(7)
for _ in range(50):
    n = random.randint(1, 60)
    lista = [random.randint(-100, 100) for _ in range(n)]
    assert subarreglo_fuerza_bruta(lista)[2] == suma_dc(lista), lista

print("Todas las pruebas pasaron")
