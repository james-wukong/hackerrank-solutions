#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

from typing import List

def bomberMan(n, grid):
    
    r, c = len(grid), len(grid[0])
    if n == 1:
        return grid
    elif n % 2 == 0:
        return ['O' * c] * r
    elif n % 4 == 3:
        # 1st-bomb pattern
        return detonate(grid)
    else:
        # 2nd-bomb pattern
        return detonate(detonate(grid))


def detonate(grid: List[str]) -> List[str]:
    m, n = len(grid), len(grid[0])
    g = [['O'] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '.':
                continue
            g[i][j] = '.'
            for ii, jj in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= ii < m and 0 <= jj < n:
                    g[ii][jj] = '.'
    return [''.join(row) for row in g]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
