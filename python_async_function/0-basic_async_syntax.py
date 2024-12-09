#!/usr/bin/env python3
"""
Python
"""
import random
"""
Integracion a funciones asincronas
"""
import asyncio
"""
Modulo para tareas asincronas
"""


async def wait_random(max_delay: int = 10) -> float:
    """

    Args:
        max_delay (int, optional): Delay maximo de espera. Defaults to 10.

    Returns:
        float: Numero esperado por la funcion
    """
    num_random = random.uniform(0, max_delay)
    await asyncio.sleep(num_random)
    return num_random
