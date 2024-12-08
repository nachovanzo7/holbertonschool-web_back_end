#!/usr/bin/env python3
"""
Python3
"""

import typing
"""
typing
"""


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """_summary_

    Args:
        multiplier (float): numero por el cual se multiplica

    Returns:
        typing.Callable[[float], float]: funcion que multiplica floats
    """
    def multi(x: float) -> float:
        return x * multiplier
    return multi
