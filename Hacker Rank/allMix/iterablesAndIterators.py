# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&isFullScreen=false&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Input Format

# The input consists of three lines. The first line contains the integer , denoting the length of the list. The next line consists of  space-separated lowercase English letters, denoting the elements of the list.

# The third and the last line of input contains the integer , denoting the number of indices to be selected.

# Output Format

# Output a single line consisting of the probability that at least one of the  indices selected contains the letter:''.

# Note: The answer must be correct up to 3 decimal places.

# Constraints



# All the letters in the list are lowercase English letters.

# Sample Input

# 4 
# a a c d
# 2
# Sample Output

# 0.8333
# Explanation

# All possible unordered tuples of length  comprising of indices from  to  are:


# Out of these 6 combinations, 5 of them contain either index 1 or index 2 which are the indices that contain the letter ''.

# Hence, the answer is 5/6.

# Code -
from itertools import combinations
n=int(input())
z=input().split()
a=int(input())
comb=list(combinations(z,a))
count=0
for i in comb:
    if i.count('a'):
        count+=1
print(count/len(comb))