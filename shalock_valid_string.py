#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter
def isValid(s):
    # Write your code here
    counts = Counter(s)
    cnt_unique = set(counts.values())
    
    # only has 1 unique count
    if len(cnt_unique) == 1:
        return 'YES'
    # only has 2 unique counts
    elif len(cnt_unique) == 2:
        cnt_unique_lst = list(cnt_unique)
        most_common = counts.most_common()
        # unique counts with diff of 1
        if abs(cnt_unique_lst[0] - cnt_unique_lst[1]) == 1:
            # counts has 2 items
            if len(counts) == 2:
                return 'YES'
            # counts has more than 2 items
            else:
                if most_common[0][1] - most_common[1][1] == 1:
                    return 'YES'
                elif most_common[-2][1] - most_common[-1][1] == 1 and most_common[-1][1] == 1:
                    return 'YES'
                else:
                    return 'NO'
        # unique counts with diff more than 1
        else:
            if most_common[-2][1] > most_common[-1][1] and most_common[-1][1] == 1:
                return 'YES'
            else:
                return 'NO'
    # more than 2 unique counts
    else:
        return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
