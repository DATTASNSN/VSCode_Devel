# https://www.hackerrank.com/challenges/capitalize/problem

# Sample Input

# chris alan
# Sample Output

# Chris Alan

# Code -
import os


def solve(s):
    # s=s.split('abcdefghijklmnopqrstuvwxyz')
    # print(s)
    # for i in range(len(s)):
    #     if s[i][0].isalpha():
    #         s[i]=s[i].title()
    # return (' '.join(s))
    print(s[:].split())
    for x in s.split():
        s = s.replace(x, x.capitalize())
    return s
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()