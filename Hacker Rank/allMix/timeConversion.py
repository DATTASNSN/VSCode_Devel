# https://www.hackerrank.com/challenges/time-conversion/problem?isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Sample Input 0

# 07:05:45PM


# Sample Output 0

# 19:05:45


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    time=s[len(s)-2:]
    s=s[:len(s)-2]
    s=s.split(":")
    if time=='PM' and s[0]<'12':
        s[0]=str(int(s[0])+12)
    if time=='AM' and s[0]>='12':
        s[0]=str(int(s[0])-12)
        if int(s[0])<10:
            s[0]='0'+s[0]
    return ':'.join(s)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
