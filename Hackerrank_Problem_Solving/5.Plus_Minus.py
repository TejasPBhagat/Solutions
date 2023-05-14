#!/bin/python3

import math
import os
import random
import re
import sys

def pm(arr):
    A = 0
    B = 0
    Z = 0
    for i in arr:
        if i > 0: 
            A += 1
        elif i == 0:
            Z += 1
        else:
            B += 1

    print("{:.6f}".format(A/n))
    print("{:.6f}".format(B/n))
    print("{:.6f}".format(Z/n))
    
    
if __name__ == '__main__':

    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    pm(arr)