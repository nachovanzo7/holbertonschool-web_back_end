#!/usr/bin/env python3
"""
Python3
"""

from typing import Iterable, Sequence, List, Tuple
"""
typing
"""


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """_summary_

    Args:
        lst (Iterable[Sequence]): iterable de secuencia

    Returns:
        List[Tuple[Sequence, int]]: lista de tuplas
    """
    return [(i, len(i)) for i in lst]
