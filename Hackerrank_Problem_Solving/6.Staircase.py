#!/bin/python3

import math
import os
import random
import re
import sys

def staircase(n):
    # Write your code here

    for i in range(1,n+1):
        for j in range(1,n+1):
            if (j <= n-i ):
                print(" ", end='')
            else:
                print("-", end='')
        print()


if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
