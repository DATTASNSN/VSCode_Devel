n=int(input())
z=list(map(int,input().split()))
z=sorted(z)
a=[]
b=[]
for i in range(n):
  if i%2==0:
    a.append(z[i])
  else:b.append(z[i])
print(*a[::-1],end=" ")
print(*b)
