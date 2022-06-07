# https://www.hackerrank.com/challenges/input/problem\


# Sample Input

# 1 4
# x**3 + x**2 + x + 1
# Sample Output

# True
# Explanation

# P(1) = 1**3 + 1**2 + 1+1 =4 = 4
# Hence, the output is True.
# Code -
# Enter your code here. Read input from STDIN. Print output to STDOUT
ui = input().split()
x = int(ui[0])
print(eval(input()) == int(ui[1]))