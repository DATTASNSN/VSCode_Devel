# https://www.hackerrank.com/challenges/polar-coordinates/problem

# Task
# You are given a complex . Your task is to convert it to polar coordinates.

# Input Format

# A single line containing the complex number . Note: complex() function can be used in python to convert the input as a complex number.

# Constraints

# Given number is a valid complex number

# Output Format

# Output two lines:
# The first line should contain the value of r.
# The second line should contain the value of o.

# Sample Input

#   1+2j
# Sample Output

#  2.23606797749979 
#  1.1071487177940904

# Code - 
import cmath
print(*cmath.polar(complex(input())), sep='\n')