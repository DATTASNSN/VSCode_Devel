# https://www.hackerrank.com/challenges/s10-interquartile-range/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

# Sample Input

# STDIN           Function
# -----           --------
# 6               arrays size n = 6
# 6 12 8 10 20 16 values = [6, 12, 8, 10, 20, 16]
# 5 4 3 2 1 5     freqs = [5, 4, 3, 2, 1, 5]
# Sample Output

# 9.0

# Code -

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s=[]
    for i in range(len(values)):
        z=freqs[i]
        for j in range(z):
            s.append(values[i])
    arr=sorted(s)
    lower_half=[]
    upper_half=[]
    if len(arr)%2!=0:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2)+1:]
    else:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2):]
    if len(lower_half)%2==0:
        q1=round((lower_half[len(lower_half)//2]+lower_half[len(lower_half)//2-1])/2)
    else:
        q1=lower_half[len(lower_half)//2]
    if len(upper_half)%2==0:
        q3=round((upper_half[len(upper_half)//2]+upper_half[len(upper_half)//2-1])/2)
    else:
        q3=upper_half[len(upper_half)//2]
    print(float(q3-q1))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
    # Print your answer to 1 decimal place within this function
    s=[]
    for i in range(len(values)):
        z=freqs[i]
        for j in range(z):
            s.append(values[i])
    arr=sorted(s)
    lower_half=[]
    upper_half=[]
    if len(arr)%2!=0:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2)+1:]
    else:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2):]
    if len(lower_half)%2==0:
        q1=round((lower_half[len(lower_half)//2]+lower_half[len(lower_half)//2-1])/2)
    else:
        q1=lower_half[len(lower_half)//2]
    if len(upper_half)%2==0:
        q3=round((upper_half[len(upper_half)//2]+upper_half[len(upper_half)//2-1])/2)
    else:
        q3=upper_half[len(upper_half)//2]
    print(float(q3-q1))
    

if __name__ == '__main__':
    n = int(input().strip())

    val = list(map(int, input().rstrip().split()))

    freq = list(map(int, input().rstrip().split()))

    interQuartile(val, freq)
