#!/usr/bin/env python3
"""
Python
"""
import asyncio
"""
Modulo para tareas asincronas
"""
task_wait_random = __import__('3-tasks').task_wait_random
"""
funcion que devuelve los segundos de delay esperados
"""

async def task_wait_n(n: int, max_delay: int):
    """

    Args:
        n (int): numero de tareas a ejecutar.
        max_delay (int): maximo tiempo de espera

    Returns:
        List[float]: lista de tiempos de espera ordenados
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
