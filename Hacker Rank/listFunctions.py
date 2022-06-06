# https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    z=[]
    for _ in range(N):
        i = list(input().split())
        if i[0] == 'insert':
            z.insert(int(i[1]),int(i[2]))
        elif i[0] == 'print':
            print(z)
        if i[0] =='remove':
            z.remove(int(i[1]))
        if i[0] == 'append':
            z.append(int(i[1]))
        if i[0] == 'sort':
            z.sort()
        if i[0] == 'pop':
            z.pop()
        if i[0] == 'reverse':
            z.reverse()
# submisiion great code
n = input()
l = []
for _ in range(n):
    s = input().split()
    cmd = s[0]
    args = s[1:]
    if cmd !="print":
        cmd += "("+ ",".join(args) +")"
        eval("l."+cmd)
    else:
        print(l)