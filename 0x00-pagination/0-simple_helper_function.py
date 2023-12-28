#!/usr/bin/env python3
"""defines a function index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """takes in page and page size and returns
    a tuple of size containing a start index and
    an end index"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
