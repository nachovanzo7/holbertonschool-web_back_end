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


def task_wait_random(max_delay: int):
    """_summary_

    Args:
        max_delay (int): segundos maximos de delays

    Returns:
        _type_: _description_
    """
    return asyncio.Task(wait_random(max_delay))
