
# https://www.hackerrank.com/challenges/python-string-formatting/problem
# sample example
#  1  1  1  1
#  2  2  2 10

# Code
def print_formatted(number):
    # your code goes here
    binlen=int(len(str(bin(number)[2:])))
    for i in range(1,number+1):
        octal = str(oct(i)[2:])
        hexa = str(hex(i)[2:])
        binary = str(bin(i)[2:])
        if hexa.islower()==True:hexa=hexa.upper()
        print(" "*(binlen-len(str(i))) + str(i),end=" ")
        print(" "*(binlen-len(octal)) + octal,end=" ")
        print(" "*(binlen-len(hexa)) + hexa,end=" ")
        print(" "*(binlen-len(binary)) + binary,end="\n")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)