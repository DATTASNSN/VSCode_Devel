# https://www.hackerrank.com/challenges/no-idea/problem


# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m  = input().split()
List = input().split()
a=set(input().split())
b=set(input().split())
count=0
#submission code
print(sum([(i in a) - (i in b) for i in List]))
#mycode
# for i in range(int(m)):
#     if a[i] in List:
#         count+=1
#     if b[i] in List:
#         count-=1
# print(count)
