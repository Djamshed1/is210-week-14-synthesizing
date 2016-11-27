#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 14 Synthesizing task 01"""

def xfibo(count):
    """A Fibonacci sequence.

    Args:
        count(int): The number of Fibonacci numbers to return.

    Returns:
        Returns integer. Each number in a Fibonacci sequence starting with 0
        and stops at number specified.

    Example:
        >>> for i in xfibo(5):
        ...     print i
        0
        1
        1
        2
        3

        >>> for i in xfibo(10):
	print i

	0
	1
	1
	2
	3
	5
	8
	13
	21
	34
	>>> 
    """
    iteration = 0
    beginnum, endnum = 0, 1
    while iteration < count:
        yield beginnum
        beginnum, endnum = endnum, beginnum + endnum
        iteration += 1
