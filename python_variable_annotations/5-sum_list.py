#!/usr/bin/env python3
"""
python
"""

from typing import List
""" 
typing
"""


def sum_list(input_list: List[float]) -> float:
    """
    Calcula la suma de los elementos de una lista de números decimales.

    Args:
        input_list (List[float]): Lista de números decimales (float) a sumar.

    Returns:
        float: La suma total de los elementos en la lista.
    """
    sum = 0
    for i in input_list:
        sum += i
    return sum
