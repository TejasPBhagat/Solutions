#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    hour, min, sec = s.split(':')
    if hour != '12' and sec[-2:] == "PM": 
        hours = int(hour) + 12 
        return "{}:{}:{}".format(hours, min, sec[-4:-2])
    elif hour == '12' and sec[-2:] == "AM":
        hours = "00"
        return "{}:{}:{}".format(hours, min, sec[-4:-2])
    else: 
        return s[:-2]
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
