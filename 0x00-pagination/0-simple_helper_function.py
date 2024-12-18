#!/usr/bin/env python3
"""
Task 0
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Retrieves index range from given page and page size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
