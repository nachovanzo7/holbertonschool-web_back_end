#!/usr/bin/env python3
"""
python
"""

from typing import List, Union
""" 
typing
"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calcula la suma de los elementos de una lista que contiene números enteros y decimales.

    Args:
        mxd_lst (List[Union[int, float]]): Lista de números que pueden ser enteros o flotantes.

    Returns:
        float: La suma total de los elementos en la lista.
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
