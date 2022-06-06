# hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

# Sample Input

# STDIN   Function
# -----   --------
# 1       t = 1
# 5       n = 5
# ebacd   grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
# fghij
# olmkn
# trpqs
# xywuv
# Sample Output

# YES
# Explanation

# The x grid in the  test case can be reordered to

# abcde
# fghij
# klmno
# pqrst
# uvwxy
# This fulfills the condition since the rows 1, 2, ..., 5 and the columns 1, 2, ..., 5 are all alphabetically sorted.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#
def gridChallenge(grid):
    # count=0
    # if len(grid)>2:
    #     for i in range(len(grid[0])):
    #         z=[]
    #         for j in range(len(grid)):
    #             z.append(grid[j][i])
    #         print(z)
    #         print(sorted(z))
    #         if z==sorted(z) or z[::-1]==sorted(z)[::-1]:
    #             count+=1
    #     if count!=len(grid[0]):
    #         return 'NO'
    #     else:return 'YES'
    # else:
    #     return 'YES'
    # Write your code here
    res = [sorted(g) for g in grid]
    res_t = [list(x) for x in zip(*res)]
    test_res_t = [sorted(t) for t in res_t]
    return 'YES' if res == sorted(res) and res_t == test_res_t else 'NO'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            chip=[]
            grid_item = input()
            for i in grid_item:
                chip.append(ord(i))
            chip=sorted(chip)
            grid.append(chip)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()
