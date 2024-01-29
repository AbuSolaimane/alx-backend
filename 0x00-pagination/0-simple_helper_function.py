#!/usr/bin/env python3
"""
this is a module
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """this is a metho"""
    nextPageStartIndex = page * page_size
    return nextPageStartIndex - page_size, nextPageStartIndex
