# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
# Sample Input 0

# 2
# abba
# abcd
# Sample Output 0

# 4
# 0
# Sample Input 1

# 2
# ifailuhkqq
# kkkk
# Sample Output 1

# 3
# 10
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sherlockAndAnagrams' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
from collections import Counter
def sherlockAndAnagrams(s):
    # Write your code here
    z=[[s[j:j+i] for j in range(len(s) - i + 1)] for i in range(1, len(s))]
    c = Counter()
    s = 0
    for lst in z:
        for e in lst:
            q = ''.join(sorted(e))
            c[q] += 1
    for e in c:
        s += int(c[e]*(c[e]-1)/2)
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
