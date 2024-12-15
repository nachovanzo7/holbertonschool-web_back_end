#!/usr/bin/env python3
"""
Python
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """

    Returns:
        float: Total runtime in seconds.
    """
    comienzo = time.perf_counter()  # Medir más preciso que event_loop

    # Ejecutar cuatro tareas en paralelo
    tasks = [
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
    ]
    await asyncio.gather(*tasks)  # Uso explícito del patrón gather(*tasks)

    fin = time.perf_counter()

    return fin - comienzo
