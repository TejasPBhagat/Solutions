#!/bin/python3

import math
import os
import random
import re
import sys

def compareTriplets(a, b):
    # Write your code here
    A = 0 
    B = 0 
    i = 0
    while i <= 2:
        if a[i] > b[i]:
            A = A + 1      
        elif a[i] < b[i]:
            B = B + 1
        elif a[i] == b[i]:
            A += 0 
            B += 0
        i = i + 1
    return A, B
        

if __name__ == '__main__':

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    print(result)
