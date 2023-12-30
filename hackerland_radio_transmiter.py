#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hackerlandRadioTransmitters' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER k
#

def hackerlandRadioTransmitters(x, k):
    transms=1
    x.sort()
    currentIdx=0
    centerCandidatePos = x[currentIdx]+k
    antennaPos = currentIdx
    while currentIdx < len(x):
        # firstly, find the position/value that between transms and transms + k
        if x[currentIdx] <= centerCandidatePos:
            # find actual antenna position closest to center
            antennaPos = x[currentIdx] 
        # then, find the ending position for new transms
        elif x[currentIdx] > antennaPos+k:
            # we've moved to a house outside of current range, next candidate
            centerCandidatePos = x[currentIdx]+k
            transms+=1
            
        currentIdx+=1

    return transms

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    x = list(map(int, input().rstrip().split()))

    result = hackerlandRadioTransmitters(x, k)

    fptr.write(str(result) + '\n')

    fptr.close()
