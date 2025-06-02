#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    izero = 0
    imayor = 0
    imenor = 0
    lenArr = len(arr)
    for i in range(lenArr):   
        if arr[i] == 0:
            izero = izero + 1
        if arr[i] > 0 : 
            imayor = imayor + 1
        if arr[i] < 0:
            imenor = imenor + 1        
    resultP = imayor / lenArr
    resultN = imenor / lenArr
    resultZ = izero / lenArr
    print(resultP) 
    print(resultN) 
    print(resultZ) 
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
