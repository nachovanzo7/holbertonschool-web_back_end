#!/usr/bin/env python3
"""
Python
"""

async_comprehension = __import__('1-async_comprehension').async_comprehension
import asyncio
import typing


async def measure_runtime() -> typing.List[float]:
    """

    Returns:
        float: tiempo de ejecucion
    """
    comienzo = asyncio.get_event_loop().time()
    
    await asyncio.gather(async_comprehension(), async_comprehension(), 
                         async_comprehension(), async_comprehension())

    fin = asyncio.get_event_loop().time()
    
    return fin - comienzo
