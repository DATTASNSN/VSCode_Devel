# https://www.hackerrank.com/challenges/30-class-vs-instance/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Input Format

# Input is handled for you by the stub code in the editor.

# The first line contains an integer,  (the number of test cases), and the  subsequent lines each contain an integer denoting the  of a Person instance.

# Constraints

# Output Format

# Complete the method definitions provided in the editor so they meet the specifications outlined above; the code to test your work is already in the editor. If your methods are implemented correctly, each test case will print  or  lines (depending on whether or not a valid  was passed to the constructor).

# Sample Input

# 4
# -1
# 10
# 16
# 18
# Sample Output

# Age is not valid, setting age to 0.
# You are young.
# You are young.

# You are young.
# You are a teenager.

# You are a teenager.
# You are old.

# You are old.
# You are old.

# Code -
class Person:
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge<0:
            initialAge=0
            print("Age is not valid, setting age to 0.")
        self.initialAge=initialAge
    def amIOld(self):
        amIOld1 = self.initialAge
        # Do some computations in here and print out the correct statement to the console
        if amIOld1<13:
            print("You are young.")
        elif amIOld1>=13 and amIOld1<18:
            print("You are a teenager.")
        elif amIOld1>=18:
            print("You are old.")
        
    def yearPasses(self):
        self.initialAge+=1
        # Increment the age of the person in here

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")