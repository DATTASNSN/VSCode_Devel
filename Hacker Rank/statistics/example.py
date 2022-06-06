s=input()
n=int(input())
z=input().split()
occurs=0
for i in range(n):
  occurs+=(ord(z[i])*s.count(z[i]))
print(occurs)
87
422
30
737
224
677
893
640
26
276
