#!/usr/bin/env python3
"""
Python
"""

def index_range(page: int, page_size: int) -> tuple:
    """

    Args:
        page (int): pagina actual
        page_size (int): tamaño de pagina

    Returns:
        tuple: tupla con inicio y fin de pagina
    """
    inicio = (page - 1) * page_size
    fin = inicio + page_size
    tupla = (inicio, fin)
    return tupla
