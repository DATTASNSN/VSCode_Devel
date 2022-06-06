# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/problem

# Tutorial

# https://www.hackerrank.com/challenges/s10-binomial-distribution-1/tutorial

# Objective
# In this challenge, we learn about binomial distributions. Check out the Tutorial tab for learning materials!

# Task
# The ratio of boys to girls for babies born in Russia is . If there is 1 child born per birth, what proportion of Russian families with exactly 6 children will have at least 3 boys?

# Write a program to compute the answer using the above parameters. Then print your result, rounded to a scale of 3 decimal places (i.e.,1.234  format).

# Enter your code here. Read input from STDIN. Print output to STDOUT

# ratio given 1.09:1
def fact(n):
    return 1 if n==0 else n*fact(n-1)
def comb(n,x):
    return fact(n)/(fact(x)*fact(n-x))
def binomial(x,n,p):
    print(comb(n,x))
    return comb(n,x) * p**x * (1-p)**(n-x)

boys,girls=1.09,1
# print("0.696")
odds=boys/girls
print(round(sum([binomial(i,6,odds/(1+odds)) for i in range(3,7)]),3))

# https://www.hackerrank.com/challenges/s10-binomial-distribution-2/problem
# A manufacturer of metal pistons finds that, on average,12%  of the pistons they manufacture are rejected because they are incorrectly sized. What is the probability that a batch of  pistons will contain:

# No more than 2 rejects?
# At least 2 rejects?
# Input Format

# A single line containing the following values (denoting the respective percentage of defective pistons and the size of the current batch of pistons):

# 12 10
# If you do not wish to read this information from stdin, you can hard-code it into your program.

# Output Format

# Print the answer to each question on its own line:

# The first line should contain the probability that a batch of 10 pistons will contain no more than 2 rejects.
# The second line should contain the probability that a batch of 10 pistons will contain at least 2 rejects.
# Round both of your answers to a scale of  decimal places (i.e.,1.234 format).
# Code -
# Above Recusion is Ok -
n,m=12,10
p=n/100
print(round(sum([binomial(i,m,p) for i in range(0,3)]),3))
print(round(sum([binomial(i,m,p) for i in range(2,m)]),3))
