#!/bin/python3

import math
import os
import random
import re
import sys

# def diagonalDifference(arr):
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    print(arr)

    list = []
    for i in range(n):
        list.append(arr[i][i])
        
    print(sum(list))