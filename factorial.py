"""
Módulo que contiene la función factorial.
"""

def factorial(n: int) -> int:
    """
    Calcula el factorial de un número entero no negativo.

    :param n: número entero del que se quiere calcular el factorial
    :return: factorial de n
    :raises TypeError: si n no es un entero
    :raises ValueError: si n es negativo
    """
    if not isinstance(n, int):
        raise TypeError("n debe ser un entero")
    if n < 0:
        raise ValueError("n no puede ser negativo")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado
