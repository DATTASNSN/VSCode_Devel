# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

# You are given an integer, . Your task is to print an alphabet rangoli of size . (Rangoli is a form of Indian folk art based on creation of patterns.)

# Different sizes of alphabet rangoli are shown below:

# #size 3

# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----

# #size 5

# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------

# #size 10

# ------------------j------------------
# ----------------j-i-j----------------
# --------------j-i-h-i-j--------------
# ------------j-i-h-g-h-i-j------------
# ----------j-i-h-g-f-g-h-i-j----------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
# --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
# ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
# ------j-i-h-g-f-e-d-e-f-g-h-i-j------
# --------j-i-h-g-f-e-f-g-h-i-j--------
# ----------j-i-h-g-f-g-h-i-j----------
# ------------j-i-h-g-h-i-j------------
# --------------j-i-h-i-j--------------
# ----------------j-i-j----------------
# ------------------j------------------

# Code - 
def print_rangoli(size):
    # your code goes here
    # length=((((size*2)-1)*2)-1)-len(c)
    # print(('-')*(length//2)+c+('-')*(length//2))
    c=[]
    for i in range(size,0,-1):
        z=[]
        for j in range(size,i-1,-1):
            z.append(chr(96+j))
        if len(z)>1:
            o=z[::-1]
            string=('-'.join(z)) + '-' + ('-'.join(o[1:]))
        else:
            string=('-'.join(z))
        length=((((size*2)-1)*2)-1)-len(string)
        modified = ('-')*(length//2) + string + ('-')*(length//2)
        c.append(modified)
        print(modified)
    c=c[::-1]
    print(*c[1:],sep="\n")
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
