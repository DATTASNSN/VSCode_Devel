# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true


def merge_the_tools(string, k):
    # your code goes here
    z=[]
    y=''
    for i in range(0,len(string),k):
        for j in range(i,i+k):
            if string[j] not in y:
                y+=string[j]
        z.append(y)
        y=''
    print(*z,sep="\n")
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)