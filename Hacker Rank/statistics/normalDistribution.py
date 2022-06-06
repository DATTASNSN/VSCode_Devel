# https://www.hackerrank.com/challenges/s10-normal-distribution-1/problem
# Tried Code -
# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import math
# mean,sd=map(int,input().split())
# variance=sd**2
# pi=3.14
# e=2.718289
# first_x=float(input())
# second_x=list(map(int,input().split()))
# first_result=0
# second_result=0
# equation1=(1/(sd*(math.sqrt(2*(pi**2)))))
# equation2=(e**(-(((first_x-mean)**2)/2*variance)))
# for i in range(19,23):
#     second_result+=equation1*(e**(-(((i-mean)**2)/2*variance)))
# print(round(second_result,3))

# Correct Code -
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
mean=20.0
stddev=2.0
h1=19.5
h21,h22=20.0,22.0

def integrate(func,b,n=10000):
    step=1/n
    if(b<0):step=-step
    n=int(abs(b)*n)
    a=0.0
    sq=0.0
    for _ in range(0,n):
        sq+=step*func(a)
        a+=step
    return abs(sq)

erf = lambda b : (2*math.pi**(-0.5)) * integrate(lambda x: math.exp(-x**2),b)
phi = lambda b : (1 + erf( (b-mean) / (stddev * 2**0.5) ))/2
lesh1 = phi(0.0) - phi(h1)
beth1h2 = phi(h22) - phi(h21)
print(f'{lesh1:.3f}')
print(f'{beth1h2:.3f}')