#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(0,n):
        for j in range(0,n-1-i):
            print(" ",end="")
        for j in range(0,i+1):
            print("#", end ="")
        print(end="\n")
if __name__ == '__main__':
    n = int(input())

    staircase(n)
