# https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/

# Sample Input
# 2
# 5 1 2
# 10 2 4

# Sample Output
# 17
# 134

t = int(input())
for i in range(t):
    n,a,b = map(int,input().split())
    x=(n*b)//(a+b)
    y=n-x
    if(abs(x*(a+b)-(n*b))>abs((x+1)*(a+b)-(n*b))):
        x=x+1
        y=n-x
    print(a*(x**2)+b*(y**2))