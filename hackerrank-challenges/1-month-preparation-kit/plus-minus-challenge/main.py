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
    positive_numbers = len([n for n in arr if n > 0])
    total_zeros = len([n for n in arr if n == 0])
    negative_numbers = len([n for n in arr if n < 0])
    print(f"%0.6f" % (positive_numbers / len(arr)))
    print(f"%0.6f" % (negative_numbers / len(arr)))
    print(f"%0.6f" % (total_zeros / len(arr)))
    # Write your code here


if __name__ == '__main__':
    n = [1, 2, 3, -1, -2, -3, 0, 0]

    plusMinus(n)
