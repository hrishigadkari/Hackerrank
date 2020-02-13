#!/bin/python3

import math
import os
import random
import re
import sys
#from decimal import *
# Complete the plusMinus function below.
#getcontext().prec = 6
def plusMinus(arr):
    pos = neg = zero = 0
    for i in range(0,n):
        if arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1
        else:
            zero += 1
    pos = pos/n
    neg = neg/n
    zero = zero/n
    print(pos, neg,zero, sep="\n")
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
