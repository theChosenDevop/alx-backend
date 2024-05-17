#!/usr/bin/env python3
"""0-simple_helper module"""


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
