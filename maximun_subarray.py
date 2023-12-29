#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def get_contiguous_max_sum(arr):
    max_sum_at_position = 0
    max_so_far = -float('inf')
    
    for num in arr:
        max_sum_at_position = max(num, num+max_sum_at_position)
        max_so_far = max(max_so_far, max_sum_at_position)
        
    return max_so_far

def get_subsequence_sum(arr):
    result = []
    for num in arr:
        if num > 0:
            result.append(num)
    if len(result) == 0:
        result.append(max(arr))
        
    return sum(result)

def maxSubarray(arr):
    # Write your code here
    return [get_contiguous_max_sum(arr), get_subsequence_sum(arr)]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
