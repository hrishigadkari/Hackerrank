#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    alice = bob = 0
    for i in range(0,len(a)):
        if a[i] < 0 or a[i] > 100 or b[i] < 0 or b[i] > 100:
            return False
        if a[i] > b[i]:
            alice += 1
        elif a[i] < b[i]:
            bob += 1
        else:
            pass
    return alice , bob

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
