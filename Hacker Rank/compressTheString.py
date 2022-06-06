
# More Information about IterTools - https://docs.python.org/2/library/itertools.html
# https://www.hackerrank.com/challenges/compress-the-string/problem
#  using groupBy function from itertools to complete this question instead of normal method to decrease time complexity

# Normal Code - 
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
count=1
for i in range(0,len(n),count):
    count=1
    while n[i+1] != n[i]:
        count+=1
    print(count)
    # print('(' + str(count) + ',' + n[i] + ')',end=" ")
    
# GroupBy Code - 
from itertools import groupby
print(*[(len(list(c)), int(k)) for k, c in groupby(input())])

# Explanation - 