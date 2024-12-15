#!/usr/bin/env python3
"""
Hypermedia pagination for a dataset of popular baby names.
"""

from typing import List, Dict  # Importaciones al inicio
import csv
import math


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Ignorar encabezado

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexado por posición de orden, comenzando en 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Devuelve datos resilientes a eliminaciones con metadatos.

        Args:
            index (int): índice inicial
            page_size (int): tamaño de la página

        Returns:
            dict: información sobre la página y metadatos
        """
        assert isinstance(index, int) and index >= 0, "entero no negativo."

        info_index = self.indexed_dataset()
        keys = sorted(info_index.keys())

        if index >= len(keys):
            return {
                "index": index,
                "data": [],
                "page_size": 0,
                "next_index": None
            }

        if index not in keys:
            index = next((k for k in keys if k >= index), None)

        start_idx = keys.index(index)
        data = []

        for i in range(start_idx, start_idx + page_size):
            if i < len(keys):
                data.append(info_index[keys[i]])

        sig_index = (keys[start_idx + page_size]
                     if start_idx + page_size < len(keys)
                     else None)

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": sig_index
        }
