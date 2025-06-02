#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def migratoryBirds(arr):
    # Create a frequency counter for the bird types
    bird_counts = Counter(arr)
    
    # Find the bird type with the highest frequency and, in case of a tie, the smallest bird ID
    most_frequent_bird = min(bird_counts, key=lambda x: (-bird_counts[x], x))
    
    return most_frequent_bird


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
