# https://www.hackerrank.com/challenges/py-the-captains-room/problem
# small problem but confused we have the single element which is present pnly one time in the list so there is a feature if the first input is 5 then 5  different elements will repeat 6 times only one element will occurs one time so we just list * 5 and set * list and subtract both and divivded with noof elements -1 
# submisiion code
k,arr = int(input()),list(map(int, input().split()))

myset = set(arr)
print(((sum(myset)*k)-(sum(arr)))//(k-1))
# mycode
# n=int(input())
# m=input().split()
# z=[]
# for i in m:
#     if i not in z:
#         if m.count(i)==1:
#             print(i)
#             break
#         z.append(i)
