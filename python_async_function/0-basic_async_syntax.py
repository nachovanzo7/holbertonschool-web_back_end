#!/usr/bin/env python3
"""
Python
"""
import asyncio
"""
Modulo para tareas asincronas
"""
import random
"""
Integracion a funciones asincronas
"""


async def wait_random(max_delay = 10):
    """

    Args:
        max_delay (int, optional): Delay maximo de espera. Defaults to 10.

    Returns:
        float: Numero esperado por la funcion
    """
    num_random = random.uniform(0, max_delay)
    await asyncio.sleep(num_random)
    return num_random
