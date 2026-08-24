def calcular_promedio(numeros: list[float]) -> float:
    """Recibe una lista de numeros y devuelve el promedio."""
    suma = 0
    for numero in numeros:
        suma = suma + numero
    return suma / len(numeros)


def main() -> None:
    lista = [1, 2, 3, 4, 5]
    print(calcular_promedio(lista))


if __name__ == "__main__":
    main()
