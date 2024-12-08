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
    Calcula la suma de los elementos de una lista de int o float

    Args:
        mxd_lst (List[Union[int, float]]): Lista de números que int o float

    Returns:
        float: La suma total de los elementos en la lista.
    """
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
