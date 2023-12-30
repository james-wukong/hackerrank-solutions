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
