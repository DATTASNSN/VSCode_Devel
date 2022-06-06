# https://www.hackerrank.com/challenges/itertools-product

# Enter your code here. Read input from STDIN. Print output to STDOUT

# Itertools Product
from itertools import combinations, combinations_with_replacement, permutations, product
a=list(map(int,input().split()))
b=list(map(int,input().split()))
print(*list(product(a,b)))

# Output
# A = [1, 2]
# B = [3, 4]

# AxB = [(1, 3), (1, 4), (2, 3), (2, 4)]



# Itertools permutations

# Input Format

# A single line containing the space separated string  and the integer value .

# Constraints


# The string contains only UPPERCASE characters.

# Output Format

# Print the permutations of the string  on separate lines.

# Sample Input

# HACK 2
# Sample Output

# AC
# AH
# AK
# CA
# CH
# CK
# HA
# HC
# HK
# KA
# KC
# KH
# Explanation

# All possible size 2 permutations of the string "HACK" are printed in lexicographic sorted order.

# Code -
# Enter your code here. Read input from STDIN. Print output to STDOUT

s= input().split()
s[0]=sorted(s[0])
l=list(permutations(s[0],int(s[1])))
for i in l:
    print(*list(i),sep="")

# combinations
# Task

# You are given a string .
# Your task is to print all possible combinations, up to size , of the string in lexicographic sorted order.

# Input Format

# A single line containing the string s and integer value k separated by a space.

# Output Format

# Print the different combinations of string s on separate lines.

# Sample Input

# HACK 2
# Sample Output

# A
# C
# H
# K
# AC
# AH
# AK
# CH
# CK
# HK

# Code - 
s= input().split()
s[0]=sorted(s[0])
l=[]
for i in range(1,int(s[1])+1):
    l=list(combinations(s[0],i))    
    for j in l:
         print(*list(j),sep="") 


# combinations_with_replacement

# Task

# You are given a string .
# Your task is to print all possible size  replacement combinations of the string in lexicographic sorted order.

# Input Format

# A single line containing the string  and integer value  separated by a space.

# Constraints


# The string contains only UPPERCASE characters.

# Output Format

# Print the combinations with their replacements of string  on separate lines.

# Sample Input

# HACK 2
# Sample Output

# AA
# AC
# AH
# AK
# CC
# CH
# CK
# HH
# HK
# KK

# Code -  
s= input().split()
s[0]=sorted(s[0])
l=list(combinations_with_replacement(s[0],int(s[1])))
for i in l:
    print(*list(i),sep="")