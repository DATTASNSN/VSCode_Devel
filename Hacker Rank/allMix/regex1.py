# https://www.hackerrank.com/challenges/incorrect-regex/problem


# Sample Input

# 2
# .*\+
# .*+
# Sample Output

# True
# False
# Explanation

# .*\+ : Valid regex.
# .*+: Has the error multiple repeat. Hence, it is invalid.

# Code-
# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
for _ in range(int(input())):
    pattren = input()
    try:
        if re.compile(pattren):
            print("True")
    except re.error:
        print("False")
            
