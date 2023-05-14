#!/bin/python3

import math
import os
import random
import re
import sys

def gradingStudents(grades):
    for i in range(len(grades)):
        if grades[i] >= 38:
            if grades[i] % 5 == 3:
                grades[i] += 2
            elif grades[i] % 5 == 4:
                grades[i] += 1
    return grades

if __name__ == '__main__':
    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)
