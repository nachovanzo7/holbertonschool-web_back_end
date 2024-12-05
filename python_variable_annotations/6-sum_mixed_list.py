#!/usr/bin/python3

from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    sum = 0
    for i in mxd_lst:
        sum += i
    return sum
