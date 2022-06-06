# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem?h_l=interview&h_r=next-challenge&h_v=zen&isFullScreen=true&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-four

# Sample Input

# STDIN       Function
# -----       --------
# 2           t = 2
# 5           n = 5
# 2 1 5 3 4   q = [2, 1, 5, 3, 4]
# 5           n = 5
# 2 5 1 3 4   q = [2, 5, 1, 3, 4]
# Sample Output

# 3
# Too chaotic

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#
# def bribing(q):
#     count=0
#     for i in range(len(q)):
#         for j in range(i+1,len(q)):
#             if q[i]>q[j]:
#                 q[i],q[j]=q[j],q[i]
#                 count+=1
#     return count
def minimumBribes(q):
    # Write your code here
    bribes=0
    for i in range(len(q)-1):
        if q[i]-i>3:
            print('Too chaotic')
            return
        j = i
        while j >= 0 and q[j+1] < q[j]:
            q[j+1], q[j] = q[j], q[j+1]
            bribes += 1
            j -= 1
    print(bribes)
if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
