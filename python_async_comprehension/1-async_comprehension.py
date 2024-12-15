#!/usr/bin/env python3
"""
Async comprehension example.
"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Colección de números aleatorios generados asincrónicamente.

    Returns:
        List[float]: Lista de números flotantes generados por async_generator.
    """
    return [x async for x in async_generator()]
