#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    positive_numbers = len(arr.filter(lambda x: x > 0))
    print(positive_numbers)
    # Write your code here


if __name__ == '__main__':
    n = [1, 1, 0, -1, -1]

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
