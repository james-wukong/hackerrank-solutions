#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
import heapq
def cookies(k, A):
    # Write your code here
    count = 0
    heapq.heapify(A)
    if A[0] >= k:
        return 0
    while len(A) > 1 and A[0] < k:
        least = heapq.heappop(A)
        sec_least = heapq.heappop(A)
        heapq.heappush(A, least + 2 * sec_least)
        count += 1
    return -1 if A[-1] < k else count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
