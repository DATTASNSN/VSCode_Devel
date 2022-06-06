# https://www.hackerrank.com/challenges/any-or-all/problem

# Sample Input

# 5
# 12 9 61 5 14 
# Sample Output

# True

# Explanation

# Condition 1: All the integers in the list are positive.
# Condition 2: 5 is a palindromic integer.

# Hence, the output is True.

# Can you solve this challenge in 3 lines of code or less?
# There is no penalty for solutions that are correct but have more than 3 li0nes.

# Code- 
n,nums=int(input()),input().split()
print(all(map(lambda x:int(x)>-1,nums)) and any(map(lambda x:x==x[::-1],nums)) )
