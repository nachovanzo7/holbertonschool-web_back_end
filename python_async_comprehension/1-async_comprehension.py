#!/usr/bin/env python3
"""
Python
"""
async_generator = __import__('0-async_generator').async_generator
"""
Async_generator
"""


async def async_comprehension():
    """

    Returns:
        list: lista de numeros generados
    """
    return [x async for x in async_generator()]
