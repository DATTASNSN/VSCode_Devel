# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true


def minion_game(string):
    kevinScore = 0
    stuartScore = 0
    length = len(string)
    for i in range(length):
        if string[i] in 'AEIOU':
            kevinScore+=length-i
        else:
            stuartScore+=length-i
    if stuartScore>kevinScore:
        print('Stuart',stuartScore,sep=" ")
    elif stuartScore<kevinScore:
        print('Kevin',kevinScore,sep=" ")
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)