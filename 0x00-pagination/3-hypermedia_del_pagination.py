#!/usr/bin/env python3
"""defines a class on pagination"""
import csv
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialzes attributes"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """two integer arguments: index with a None
        default value and page_size with default value of 10
        return a dictionary with the following key-value pairs"""
        dataset = self.dataset()
        max_index = len(dataset) - 1

        if index is None:
            index = 0
        else:
            assert 0 <= index <= max_index

        next_index = min(index + page_size, max_index + 1)
        current_page = dataset[index:next_index]

        return {
            "index": index,
            "next_index": next_index,
            "page_size": page_size,
            "data": current_page
        }
