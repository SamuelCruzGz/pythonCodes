#!/bin/python3

import math
import os
import random
import re
import sys
import functools
#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    newArrayI = []
    newArrayJ = []
    for i in range(len(arr)):  
            
        for j in range(len(arr)):
       
            jArray = j+i
           
            if i == j:
                newArrayI.append(arr[i][j])  
                resultI = functools.reduce(lambda counter, item : counter + item, newArrayI)                 
            if jArray == len(arr)-1:
                newArrayJ.append(arr[i][j])
                resultJ = functools.reduce(lambda counter, item : counter + item, newArrayJ)         
        
        total = abs(resultI-resultJ)
    return total
             
    print(result)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
