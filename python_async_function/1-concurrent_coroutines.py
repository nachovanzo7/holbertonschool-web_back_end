#!/usr/bin/env python3
"""
Python
"""
import asyncio
"""
Modulo para tareas asincronas
"""
wait_random = __import__('0-basic_async_syntax').wait_random
"""
Funcion que devuelve los segundos de delay esperados
"""


async def wait_n(n: int, max_delay: int):
    """_summary_

    Args:
        n (int): Cantidad de veces que se ejecuta la funcion wait_random
        max_delay (int): numero maximo para esperar en wait_random

    Returns:
        list: lista de segundos esperados por funcion wait_random
    """
    lista = []
    for i in range(0, n):
        lista.append(await wait_random(max_delay))
    return lista
