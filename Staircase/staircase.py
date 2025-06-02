#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    count = 0
    space = n 
    
    for i in range(n):
        count += 1
        space -= 1
        
        print(" "*space+ "#"*count)
        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
