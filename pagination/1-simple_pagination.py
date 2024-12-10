import csv
import math
from typing import List

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


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """

        Args:
            page (int): numero de pagina
            page_size (int): size de cada pagina

        Returns:
            List[List]: dataset
        """
        assert isinstance(page, int) and page > 0, "Page debe ser un entero positivo"
        assert isinstance(page_size, int) and page_size > 0, "Tamaño de pagina debe ser un entero positivo"

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]
