# https://www.hackerrank.com/challenges/python-sort-sort/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
# Sample Input 0

# 5 3
# 10 2 5
# 7 1 0
# 9 9 9
# 1 23 12
# 6 5 9
# 1
# Sample Output 0

# 7 1 0
# 10 2 5
# 6 5 9
# 9 9 9
# 1 23 12
# Explanation 0

# The details are sorted based on the second attribute, since  is zero-indexed.

# Code -
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import OrderedDict


if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())
    c={}
    for i in range(n):
        if arr[i][k] not in c:
            c[arr[i][k]]=[arr[i]]
        else:
            c[arr[i][k]].append(arr[i])
    dict1 = OrderedDict(sorted(c.items()))
    for i in dict1.values():
        for j in i:
            print(*j)
            
            
