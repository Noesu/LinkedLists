from random import uniform
from time import monotonic

import PL
import PL2
import PL3

COORDS_RANGE = 1000000

coords = [(round(uniform(0, 100), 2), round(uniform(0, 100), 2)) for _ in range(COORDS_RANGE)]

def test_create_pathlines():
    start = monotonic()
    PL.PathLines(*[PL.LineTo(*point) for point in coords])
    finish = monotonic()
    print(f"Creating route with coords initialization, using standard list of {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

def test_add_pathlines():
    start = monotonic()
    route = PL.PathLines()
    for point in coords:
        route.add_line(PL.LineTo(*point))
    finish = monotonic()
    print(f"Creating route with empty initialization and separate coords adding, using standard list of {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

def test_create_pathlines2():
    start = monotonic()
    PL2.PathLines(*[PL2.LineTo(*point) for point in coords])
    finish = monotonic()
    print(f"Creating route with coords initialization, using doubly-linked list of {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

def test_add_pathlines2():
    start = monotonic()
    route = PL2.PathLines()
    for point in coords:
        route.add_line(PL2.LineTo(*point))
    finish = monotonic()
    print(f"Creating route with empty initialization and separate coords adding, using doubly-linked list of {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

def test_create_pathlines3():
    start = monotonic()
    PL3.PathLines(*[PL3.LineTo(*point) for point in coords])
    finish = monotonic()
    print(f"Creating route with coords initialization, using Deque and {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

def test_add_pathlines3():
    start = monotonic()
    route = PL.PathLines()
    for point in coords:
        route.add_line(PL3.LineTo(*point))
    finish = monotonic()
    print(f"Creating route with empty initialization and separate coords adding, using Deque and {COORDS_RANGE} lines.", end='   ')
    print(f'{round((finish - start) * 1000, 2)} ms.')

test_create_pathlines()
test_add_pathlines()
test_create_pathlines2()
test_add_pathlines2()
test_create_pathlines3()
test_add_pathlines3()