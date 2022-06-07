# # https://www.hackerrank.com/challenges/reduce-function/problem

# 1. add(a, b) :- This functions returns addition of the given arguments.
# Operation – a + b.

# 2. sub(a, b) :- This functions returns difference of the given arguments.
# Operation – a – b.

# 3. mul(a, b) :- This functions returns product of the given arguments.
# Operation – a * b.


# # Python code to demonstrate working of 
# # add(), sub(), mul()
  
# # importing operator module 
# import operator
  
# # Initializing variables
# a = 4
  
# b = 3
  
# # using add() to add two numbers
# print ("The addition of numbers is :",end="");
# print (operator.add(a, b))
  
# # using sub() to subtract two numbers
# print ("The difference of numbers is :",end="");
# print (operator.sub(a, b))
  
# # using mul() to multiply two numbers
# print ("The product of numbers is :",end="");
# # print (operator.mul(a, b))

# fraction multiplication
from fractions import Fraction
from functools import reduce
import operator
def product(fracs):
    t = reduce(operator.mul,fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)