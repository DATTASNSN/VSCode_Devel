# https://www.hackerrank.com/challenges/re-start-re-end/problem

# Sample Input

# aaadaa
# aa
# Sample Output

# (0, 1)  
# (1, 2)
# (4, 5)

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s=input()
k=input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',s):
    anymatch = 'Yes'
    print("(" + str(m.start(1))+", "+str(m.end(1)-1) + ")")
if anymatch == 'No':
    print ("(-1, -1)")

