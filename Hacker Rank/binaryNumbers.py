# https://www.hackerrank.com/challenges/30-binary-numbers/problem?isFullScreen=true

# Sample Input 1

# 5
# Sample Output 1

# 1
# Sample Input 2

# 13
# Sample Output 2

# 2
# Explanation

# Sample Case 1:
# The binary representation of 5 is 101, so the maximum number of consecutive 1's is 1.

# Sample Case 2:
# The binary representation of 13 is 1011, so the maximum number of consecutive 1's is 2.

# Code -
#!/bin/python3

import math
import os
import random
import re
import sys
n = int(input().strip())
binary=str(bin(n)[2:])
binary=binary.split('0')
print(len(max(binary)))