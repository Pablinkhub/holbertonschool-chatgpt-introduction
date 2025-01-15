#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calcula el factorial de un número dado de manera recursiva.

    Parámetros:
    n (int): El número entero no negativo del cual se calcula el factorial.

    Retorna:
    int: El factorial del número ingresado.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Obtiene el número del argumento de la línea de comandos, calcula su factorial y lo imprime.
f = factorial(int(sys.argv[1]))
print(f)
