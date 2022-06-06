# https://www.hackerrank.com/challenges/mark-and-toys/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting

# Sample Input

# 7 50
# 1 12 5 111 200 1000 10
# Sample Output

# 4
# Explanation

# He can buy only 4 toys at most. These toys have the following prices: 1,2,5,10.

# Code -
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumToys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY prices
#  2. INTEGER k
#

def maximumToys(prices, k):
    # Write your code here
    
    prices=sorted(prices)
    addition=0
    z=0
    for i in range(len(prices)):
        while addition+prices[i]<k and i<len(prices)-1:
            addition+=prices[i]
            i+=1
        z=i
        break
    return z
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
