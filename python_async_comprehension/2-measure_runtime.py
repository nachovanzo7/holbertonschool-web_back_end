#!/usr/bin/env python3
"""
Python
"""
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension
"""
Async_comprehension
"""


async def measure_runtime() -> float:
    """

    Returns:
        float: tiempo de ejecucion
    """
    comienzo = asyncio.get_event_loop().time()
    
    await asyncio.gather(async_comprehension(), async_comprehension(), 
                         async_comprehension(), async_comprehension())

    fin = asyncio.get_event_loop().time()
    
    return fin - comienzo
