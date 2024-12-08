#!/usr/bin/env python3
"""
Python3
"""

import typing
"""
typing
"""


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """

    Args:
        k (str): es un string
        v (typing.Union[int, float]): un entero o float

    Returns:
        typing.Tuple[str, float]: devuelve una tupla de string y float
    """
    tupla = (k, v ** 2)
    return tupla