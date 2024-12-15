#!/usr/bin/env python3
"""
Python
"""

import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measure the total runtime of running async_comprehension four times in parallel.

    Returns:
        float: Total runtime in seconds.
    """
    comienzo = time.perf_counter() #Medir mas preciso que event_loop

    # Ejecutar cuatro tareas en paralelo
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    fin = time.perf_counter()
    
    return fin - comienzo
