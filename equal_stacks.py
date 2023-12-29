#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#
def get_running_total(stack):
    total = []
    for key, item in enumerate(stack[::-1]):
        tmp = total[key-1] if key>=1 else 0
        total.append(item+tmp)
        
    return total

def equalStacks(h1, h2, h3):
    # Write your code here
    h1_running = get_running_total(h1)
    h2_running = get_running_total(h2)
    h3_running = get_running_total(h3)
    
    result = set(h1_running).intersection(set(h2_running), set(h3_running))
    
    return sorted(result)[-1] if len(result) > 0 else 0
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
