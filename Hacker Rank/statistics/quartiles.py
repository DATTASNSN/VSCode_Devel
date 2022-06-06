# https://www.hackerrank.com/challenges/s10-quartiles/problem?isFullScreen=true
# Sample Input

# STDIN                   Function
# -----                   --------    
# 9                       arr[] size n = 9 
# 3 7 8 5 12 14 21 13 18  arr = [3, 7, 8, 5, 12, 14, 21, 13,18]
# Sample Output

# 6
# 12
# 16

# Code-

import os


def quartiles(arr):
    arr=sorted(arr)
    lower_half=[]
    upper_half=[]
    q2=0
    if len(arr)%2!=0:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2)+1:]
        q2=arr[len(arr)//2]
    else:
        lower_half=arr[:len(arr)//2]
        upper_half=arr[(len(arr)//2):]
        q2=round((arr[len(arr)//2]+arr[len(arr)//2-1])/2)
    if len(lower_half)%2==0:
        q1=round((lower_half[len(lower_half)//2]+lower_half[len(lower_half)//2-1])/2)
    else:
        q1=lower_half[len(lower_half)//2]
    if len(upper_half)%2==0:
        q3=round((upper_half[len(upper_half)//2]+upper_half[len(upper_half)//2-1])/2)
    else:
        q3=upper_half[len(upper_half)//2]
    return q1,q2,q3
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    data = list(map(int, input().rstrip().split()))

    res = quartiles(data)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
