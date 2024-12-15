#!/usr/bin/env python3
"""
Python
"""

import random
from typing import Generator


def async_generator() -> Generator[float, None, None]:
    """
    Generador síncrono que produce números aleatorios entre 0 y 10.

    Yields:
        float: Random float.
    """
    for _ in range(10):
        yield random.uniform(0, 10)
