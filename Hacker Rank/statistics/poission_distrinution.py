# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/problem?h_r=next-challenge&h_v=zen&isFullScreen=true
# Tutorial
# https://www.hackerrank.com/challenges/s10-poisson-distribution-1/tutorial
# Objective
# In this challenge, we learn about Poisson distributions. Check out the Tutorial tab for learning materials!

# Task
# A random variable,X , follows Poisson distribution with mean of 2.5. Find the probability with which the random variable X is equal to 5.
# Code - 
from importlib.metadata import distribution


def fact(n):
    return 1 if n==0 else n*fact(n-1)
average=float(input())
actual=float(input())
e=2.718289
print(round(((average**actual)*(e**(-average)))/fact(actual),3))

# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem?h_r=next-challenge&h_v=zen&isFullScreen=true&h_r=next-challenge&h_v=zen
# Special Case in poission distribution-
# Consider some Poisson random variable,X . Let E[X] be the expectation of X. Find the value of E[X**2]=actual + actual**2.
# Enter your code here. Read input from STDIN. Print output to STDOUT
A,B=map(float,input().split())
result1=40 * (A+(A**2))
result2=40 * (B+(B**2))
print(round(160+result1,3))
print(round(128+result2,3))