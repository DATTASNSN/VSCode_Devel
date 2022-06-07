# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?isFullScreen=true

# Example
# a=[6,4,1]
# swap    a       
# 0       [6,4,1]
# 1       [4,6,1]
# 2       [4,1,6]
# 3       [1,4,6]
# The steps of the bubble sort are shown above. It took 3 swaps to sort the array. Output is:

# Array is sorted in 3 swaps.  
# First Element: 1  
# Last Element: 6  
# Function Description

# Complete the function countSwaps in the editor below.

# countSwaps has the following parameter(s):

# int a[n]: an array of integers to sort

# Code -

#!/bin/python3

import math
import os
import random
import re
import sys
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    count=0
    z=sorted(a)
    if z==a:
        print('Array is sorted in ' + str(count)+ ' swaps.')
        print('First Element: ' + str(a[0]))
        print('Last Element: ' + str(a[len(a)-1]))
    else:
        for i in range(len(a)):
            for j in range(len(a)-1):
                if(a[j]>a[j+1]):
                    temp=a[j]
                    a[j]=a[j+1]
                    a[j+1]=temp
                    count+=1
                if z==a:
                    break
        print('Array is sorted in ' + str(count)+ ' swaps.')
        print('First Element: ' + str(a[0]))
        print('Last Element: ' + str(a[len(a)-1]))
        
        
if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
