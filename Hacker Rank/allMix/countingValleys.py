# https://www.hackerrank.com/challenges/counting-valleys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen
# Sample Input

# 8
# UDDDUDUU
# Sample Output

# 1
# Explanation

# If we represent _ as sea level, a step up as /, and a step down as \, the hike can be drawn as:

# _/\      _
#    \    /
#     \/\/
# The hiker enters and leaves one valley.

# Code -
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    count=0
    valley_count=0
    valley_start=0
    for i in path:
        if i=='D':
            count-=1
        elif i=='U':
            count+=1
        if count==-1:
            valley_start=1
        if count==0 and valley_start==1:
            valley_count+=1
            valley_start=0
    return valley_count
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
