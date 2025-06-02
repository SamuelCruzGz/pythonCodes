#!/bin/python3
import functools
import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    # Write your code here 
    newDict = {}
    count = 0
    for i in ar:
        res = ar.count(i)         
        newDict[i] = res
        count +=1
    newList = list(newDict.values())
    result = [math.floor(i / 2) for i in newList]
    sumResult = functools.reduce(lambda a, b: a + b, result)
    return sumResult
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
