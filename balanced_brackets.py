#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def isBalanced(s):
    # Write your code here
    brackets = {'{': '}', '(': ')', '[': ']'}
    stack = []
    
    for char in s:
        if char in brackets.keys():
            stack.append(char)
        elif char in brackets.values():
            if len(stack) == 0:
                return 'NO'
            open_char = stack.pop()
            if char != brackets[open_char]:
                return 'NO'
        else:
            return 'NO'
            
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
