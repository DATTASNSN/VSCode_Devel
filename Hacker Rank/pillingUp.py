# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true

# Input Format

# The first line contains a single integer , the number of test cases.
# For each test case, there are  lines.
# The first line of each test case contains , the number of cubes.
# The second line contains  space separated integers, denoting the sideLengths of each cube in that order.

# Output Format

# For each test case, output a single line containing either Yes or No.

# Sample Input

# STDIN        Function
# -----        --------
# 2            T = 2
# 6            blocks[] size n = 6
# 4 3 2 1 3 4  blocks = [4, 3, 2, 1, 3, 4]
# 3            blocks[] size n = 3
# 1 3 2        blocks = [1, 3, 2]
# Sample Output

# Yes
# No
# Explanation

# In the first test case, pick in this order: left - 4, right -4 , left - 3, right - 3, left - 2, right - 1.
# In the second test case, no order gives an appropriate arrangement of vertical cubes.  will always come after either 1 or 2.
for _ in range(int(input())):
    n=int(input())
    blocks=list(map(int,input().split()))
    if max(blocks)==blocks[0] or max(blocks)==blocks[n-1]:
        print("Yes")
    else:
        print("No")