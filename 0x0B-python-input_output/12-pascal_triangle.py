#!/usr/bin/python3
"""a function for pascale tringal ."""


def pascal_triangle(n):
    """rept n tringals.

    Retn a list of integers.
    """
    if n <= 0:
        return []

    tri = [[1]]
    while len(tri) != n:
        tri = tri[-1]
        tmp = [1]
        for i in range(len(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        tri.append(tmp)
    return tri
