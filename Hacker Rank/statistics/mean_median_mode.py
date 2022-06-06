# https://www.hackerrank.com/challenges/s10-basic-statistics/forum

# Using Numpy 
import numpy as np
from scipy import stats

size = int(input())
numbers = list(map(int, input().split()))
print(np.mean(numbers))
print(np.median(numbers))
print(int(stats.mode(numbers)[0]))

# Mycode --
n=int(input())
m=list(map(int,input().split()))
mean=sum(m)/n
m=sorted(m)
if n%2==0:
    median=(m[n//2]+m[(n//2)-1])/2
print(mean)
print(median)
print(int(stats.mode(m)[0]))