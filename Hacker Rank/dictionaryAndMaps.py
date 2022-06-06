# https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

# Sample Input

# 3
# sam 99912222
# tom 11122222
# harry 12299933
# sam
# edward
# harry
# Sample Output

# sam=99912222
# Not found
# harry=12299933

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
dictionary={}
for _ in range(n):
    z=input().split()
    dictionary[z[0]]=z[1]
while True:
  # Can Use while True and try and except to decrease some time complexity
    try:
        inpt = input()
        if inpt in dictionary:
            print(inpt+"="+dictionary[inpt])
        else:
            print("Not found")
    except EOFError:
        break
