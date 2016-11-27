#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""week 14 sythesizing task 02"""

import task_01

def fibo(count):
    """A list comprehension to generate Fibonacci numbers.

    Args:
        count (int): The total number of Fibonacci numbers to return.

    Returns:
        list: return a list comprehension that uses task_01.xfibo() to
        generate count Fibonacci numbers and return them all in a list.

    Examples:
        >>> fibo(5)
        [0, 1, 1, 2, 3]
        >>> fibo(10)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
        >>> fibo(15)
        [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]
    """
    return [num for num in task_01.xfibo(count)]
