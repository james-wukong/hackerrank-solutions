#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'legoBlocks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#

def legoBlocks(n, m):
    MOD = 10**9 + 7
    r = [0] * (m + 1)
    a = [0] * (m + 1)

    a[0] = 1
    # total sum of position equals to sum of previous positions
    for i in range(1, m+1):
        a[i] += a[i-1] if i-1>=0 else 0
        a[i] += a[i-2] if i-2>=0 else 0
        a[i] += a[i-3] if i-3>=0 else 0
        a[i] += a[i-4] if i-4>=0 else 0
        
    for i in range(1, m+1):
        a[i] = a[i] % MOD
        a[i] = a[i] ** n
        a[i] = a[i] % MOD
    
    r[1] = 1
    for i in range(2, m+1):
        r[i] = a[i]
        for k in range(1, i):
            r[i] -= r[k]*a[i-k]
        r[i] = r[i] % MOD
        
    return r[m] % MOD

def legoBlocks_v2(n, m):
    MOD = (10**9 +7)

    # Step 1: O(W)       
    # The number of combinations to build a single row
    # As only four kinds of sizes, so
    # base case: 
    # if width is 0, combination is 1
    # if width is 1, combination is 1
    # if width is 2, combination is 2
    # if width is 3, combination is 4
    row_combinations = [1, 1, 2, 4]
    
    # Build row combinations up to current wall's width
    while len(row_combinations) <= m: 
        row_combinations.append(sum(row_combinations[-4:]) % MOD)
    
    # Step 2: O(W)
    # Compute total combinations 
    # for constructing a wall of height N of varying widths
    total = [pow(c, n, MOD) for c in row_combinations]
    
    # Step 3: O(W^2)
    # Find the number of unstable wall configurations 
    # for a wall of height N of varying widths
    unstable = [0, 0]
    
    # Divide the wall into left part and right part,
    # and calculate the combination of left part and right part.
    # From width is 2, we start to consider about violation.
    for i in range(2, m + 1):
        # i: current total width
        # j: left width
        # i - j: right width
        # f: (left part - previous vertical violation)*right part
        f = lambda j: (total[j] - unstable[j]) * total[i - j]
        result = sum(map(f, range(1, i)))
        unstable.append(result % MOD)
    
    # Print the number of stable wall combinations
    return (total[m] - unstable[m]) % MOD

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = legoBlocks(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()
