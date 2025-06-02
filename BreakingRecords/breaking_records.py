#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):
    # Write your code here
    lower = []
    higher = []
    lowest_score = scores[0]
    highest_score = scores[0]
    for i in scores[1:]:
        if i < lowest_score:
            lower.append(i)
            lowest_score = i
        elif i > highest_score:
            higher.append(i)
            highest_score = i            
    return len(higher), len(lower)
            
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
