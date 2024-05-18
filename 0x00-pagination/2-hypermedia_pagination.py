#!/usr/bin/env python3
"""1-simple_pagination module"""
import csv
import math
from typing import List, Dict


def index_range(page: int, page_size: int) -> tuple:
    """
    Function finds the index range of the start and end of a page

    Parameters:
        page [int]: The page number
        page_size [int]: The page size

    Returns:
        tuple of start index and end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get Pages of popular baby names from
            dataset
        """
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)

        if (start_index > len(self.dataset()) or
                (end_index > len(self.dataset()))):
            return []

        data = self.dataset()
        return list(data[start_index:end_index])

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """Returns dictionary of meta data"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0

        start_index, end_index = index_range(page, page_size)

        if (start_index > len(self.dataset()) or
                (end_index > len(self.dataset()))):
            return []

        dataset = self.dataset()
        data = dataset[start_index:end_index]
        total_pages = (len(dataset)) // page_size

        return {'page_size': page_size,
                'page': page,
                'data': data,
                'next_page': page + 1 if end_index < len(dataset) else None,
                'prev_page': page - 1 if page > 1 else None,
                'total_pages': total_pages
                }
