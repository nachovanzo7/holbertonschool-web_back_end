#!/usr/bin/env python3
"""
Python
"""
import asyncio
"""
Modulo para tareas asincronas
"""
wait_n = __import__('1-concurrent_coroutines').wait_n
"""
Funcion que devuelve una lista de segundos de delay esperados
"""


def measure_time(n: int, max_delay: int) -> float:
    """

    Args:
        n (int): cantidad de veces ejecutado wait_random
        max_delay (int): segundos maximos de delay

    Returns:
        float: segundos totales esperados
    """
    lista = asyncio.run(wait_n(n, max_delay))
    suma = sum(lista)

    if n > 0:
        return suma / n
    else:
        return 0
