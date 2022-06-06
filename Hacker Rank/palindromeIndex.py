import os


def palindromeIndex(s):
    # Write your code here
    # if s==s[::-1]:
    #     return -1
    # else:
    #     for i in range(len(s)):
    #         z = s[:i] +s[i+1:]
    #         if z == z[::-1]:
    #             return i
    p=0
    while p<=len(s)//2:
        q = len(s) - p - 1
        if s[p] != s[~p]:
            if s[p+1:q+1] == s[q:p:-1]:
                return p
            elif s[p:q] == s[p:q][::-1]:
                return q
            else:
                return -1
        p+=1
    return -1
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()
