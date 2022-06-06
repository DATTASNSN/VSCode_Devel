# Geometric Distribution = ((q**(n-1))*p)

# https://www.hackerrank.com/challenges/s10-geometric-distribution-1/problem
# Input Format

# The first line contains the respective space-separated numerator and denominator for the probability of a defect, and the second line contains the inspection we want the probability of being the first defect for:

# 1 3
# 5
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print a single line denoting the answer, rounded to a scale of 3 decimal places (i.e.,1.234  format).
# Enter your code here. Read input from STDIN. Print output to STDOUT

# To find the 1st defect on the 5th production  
n,m=map(int,input().split())
p=n/m
q=1-p
x=int(input())-1
print(round(((q**x)*p),3))

#  probability that the  defect is found during the first 5 inspections?
# same input difference print function
print(round(sum([(q**(i-1))*p for i in range(1,x+1)]),3))



