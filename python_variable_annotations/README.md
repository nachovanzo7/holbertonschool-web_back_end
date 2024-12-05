Función Floor en Python

Este repositorio contiene una función en Python llamada floor que calcula el piso de un valor flotante dado. La implementación está completamente anotada con tipos, garantizando claridad y compatibilidad con herramientas de chequeo estático como mypy.

Descripción General

La función floor toma un único argumento de tipo float y devuelve el entero más grande que sea menor o igual al valor flotante dado.

Características

Totalmente anotada con tipos para mayor claridad y chequeo estático.

Utiliza la función incorporada math.floor de Python para obtener resultados precisos.

Implementación simple y eficiente.

Uso

Firma de la Función

floor(n: float) -> int

Parámetros

n (float): El número del cual se necesita calcular el piso.

Retorno

int: El entero más grande que sea menor o igual a n.

Ejemplo

A continuación, un ejemplo de cómo usar la función floor:

from 2-floor import floor
import math

ans = floor(3.14)

print(ans == math.floor(3.14))  # Salida: True
print(floor.__annotations__)    # Salida: {'n': <class 'float'>, 'return': <class 'int'>}
print("floor(3.14) devuelve {} que es un {}".format(ans, type(ans)))

Salida esperada:

True
{'n': <class 'float'>, 'return': <class 'int'>}
floor(3.14) devuelve 3, que es un <class 'int'>
