#!/usr/bin/env python3
"""
Python
"""
import random
from typing import AsyncGenerator
"""
Integracion a funciones asincronas
"""
import asyncio
"""
Modulo para tareas asincronas
"""


async def async_generator() -> AsyncGenerator[float, None]:
    """

    Yields:
        AsyncGenerator: generador
    """
    for i in range(10):
        await asyncio.sleep(1)
        num = random.uniform(0, 10)
        yield num
