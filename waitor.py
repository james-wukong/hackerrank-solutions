#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'waiter' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY number
#  2. INTEGER q
#
def isprime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def get_primes(num):
    idx = 2
    primes = []
    while len(primes) <= num:
        if isprime(idx):
            primes.append(idx)
        idx += 1
    return primes
    
def waiter(number, q):
    # Write your code here
    answers, A, B = [], [], []
    primes = get_primes(len(number))
    for i in range(q):
        if i > 0:
            number, A, B = A, [], []
        for item in number[::-1]:
            if item % primes[i] == 0:
                B.append(item)
            else:
                A.append(item)
        answers += B[::-1]
        
    answers += A[::-1]
    
    return answers

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    number = list(map(int, input().rstrip().split()))

    result = waiter(number, q)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
