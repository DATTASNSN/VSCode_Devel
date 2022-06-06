# https://www.hackerrank.com/challenges/designer-door-mat/problem?h_r=next-challenge&h_v=zen
# ------------.|.------------
# ---------.|..|..|.---------
# ------.|..|..|..|..|.------
# ---.|..|..|..|..|..|..|.---
# ----------WELCOME----------
# ---.|..|..|..|..|..|..|.---
# ------.|..|..|..|..|.------
# ---------.|..|..|.---------
# ------------.|.------------

# Code
# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split()
n,m=int(n),int(m)
num=[]
z=[]
for i in range(n):
    if i%2:num.append(i+1)
num=num[::-1]
for i in range(int(n)//2):
    middle=n-num[i]
    lr=m-middle*3
    z.append(('-'*(lr//2)) + '.|.'*middle +('-'*(lr//2)))
    
print(*z,sep="\n")
m=m-7
print(str('-'*(m//2))+'WELCOME'+str('-'*(m//2)))
print(*z[::-1],sep="\n")

# submission code
n, m = map(int,input().split())
pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))