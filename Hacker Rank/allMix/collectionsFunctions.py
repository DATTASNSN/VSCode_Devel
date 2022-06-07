# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true

# collections.Counter()

# >>> from collections import Counter
# >>> 
# >>> myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# >>> print Counter(myList)
# Counter({2: 4, 3: 4, 1: 3, 4: 2, 5: 1})
# >>>
# >>> print Counter(myList).items()
# [(1, 3), (2, 4), (3, 4), (4, 2), (5, 1)]
# >>> 
# >>> print Counter(myList).keys()
# [1, 2, 3, 4, 5]
# >>> 
# >>> print Counter(myList).values()
# [3, 4, 4, 2, 1]

# Problem
# Sample Input

# 10
# 2 3 4 5 6 8 7 6 5 18
# 6
# 6 55
# 6 45
# 6 55
# 4 40
# 18 60
# 10 50
# Sample Output

# 200
# Explanation

# Customer 1: Purchased size 6 shoe for $55.
# Customer 2: Purchased size 6 shoe for $45.
# Customer 3: Size 6 no longer available, so no purchase.
# Customer 4: Purchased size 4 shoe for $40.
# Customer 5: Purchased size 18 shoe for $60.
# Customer 6: Size 10 not available, so no purchase.

# Total money earned =  55+ 45 +40+60 = 200

# Code- 
# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter, deque,namedtuple,OrderedDict
no_of_shoes=int(input())
sizes_of_shoes_in_shop = list(map(int,input().split()))
no_of_customers=int(input())
countered_list=dict(Counter(sizes_of_shoes_in_shop))
raghu_earned_money=0
for _ in range(no_of_customers):
    shoe_size,price=input().split()
    if int(shoe_size) in countered_list:
        if countered_list[int(shoe_size)] != 0:
            countered_list[int(shoe_size)] -= 1
            raghu_earned_money+=int(price)
print(raghu_earned_money)


# collections.namedtuple()
# Basically, namedtuples are easy to create, lightweight object types.
# They turn tuples into convenient containers for simple tasks.
# With namedtuples, you don’t have to use integer indices for accessing members of a tuple.

# Example -



# Code 01

# >>> from collections import namedtuple
# >>> Point = namedtuple('Point','x,y')
# >>> pt1 = Point(1,2)
# >>> pt2 = Point(3,4)
# >>> dot_product = ( pt1.x * pt2.x ) +( pt1.y * pt2.y )
# >>> print dot_product
# 11
# Code 02

# >>> from collections import namedtuple
# >>> Car = namedtuple('Car','Price Mileage Colour Class')
# >>> xyz = Car(Price = 100000, Mileage = 30, Colour = 'Cyan', Class = 'Y')
# >>> print xyz
# Car(Price=100000, Mileage=30, Colour='Cyan', Class='Y')
# >>> print xyz.Class
# Y

# Code - 

no_of_students=int(input())
props=input().split()
student = namedtuple('student',[props[0],props[1],props[2],props[3]])
marks=0
for i in range(no_of_students):
    data=input().split()
    req_list=student(data[0],data[1],data[2],data[3])
    marks+=int(req_list.MARKS)
print(float(marks/no_of_students))

# collections.OrderedDict
# An OrderedDict is a dictionary that remembers the order of the keys that were inserted first. If a new entry overwrites an existing entry, the original insertion position is left unchanged.

# Example

# >>> from collections import OrderedDict
# >>> 
# >>> ordinary_dictionary = {}
# >>> ordinary_dictionary['a'] = 1
# >>> ordinary_dictionary['b'] = 2
# >>> ordinary_dictionary['c'] = 3
# >>> ordinary_dictionary['d'] = 4
# >>> ordinary_dictionary['e'] = 5
# >>> 
# >>> print ordinary_dictionary
# {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4}
# >>> 
# >>> ordered_dictionary = OrderedDict()
# >>> ordered_dictionary['a'] = 1
# >>> ordered_dictionary['b'] = 2
# >>> ordered_dictionary['c'] = 3
# >>> ordered_dictionary['d'] = 4
# >>> ordered_dictionary['e'] = 5
# >>> 
# >>> print ordered_dictionary
# OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Problem
# Input Format

# The first line contains the number of items, .
# The next  lines contains the item's name and price, separated by a space.

# Constraints


# Output Format

# Print the item_name and net_price in order of its first occurrence.

# Sample Input

# 9
# BANANA FRIES 12
# POTATO CHIPS 30
# APPLE JUICE 10
# CANDY 5
# APPLE JUICE 10
# CANDY 5
# CANDY 5
# CANDY 5
# POTATO CHIPS 30
# Sample Output

# BANANA FRIES 12
# POTATO CHIPS 60
# APPLE JUICE 20
# CANDY 20

# Code-
n=int(input())
dictionary = {}
dictionary = dict(OrderedDict())
for i in range(n):
    z=input().split()
    a=z[:len(z)-1]
    stra=''
    for s in a:
        stra+=s+' '
        
    b=z[len(z)-1:]
    if stra in dictionary:
        dictionary[stra]+=int(b[0])
    else:
        dictionary[stra]=int(b[0])
for i in dictionary:
    print(i,end="")
    print(dictionary[i])

# https://www.hackerrank.com/challenges/py-collections-deque/problem?h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&isFullScreen=false

# collections.deque()
# A deque is a double-ended queue. It can be used to add or remove elements from both ends.

# Deques support thread safe, memory efficient appends and pops from either side of the deque with approximately the same  performance in either direction.

# Click on the link to learn more about deque() methods.
# Click on the link to learn more about various approaches to working with deques: Deque Recipes.

# Example

# Code

# >>> from collections import deque
# >>> d = deque()
# >>> d.append(1)
# >>> print d
# deque([1])
# >>> d.appendleft(2)
# >>> print d
# deque([2, 1])
# >>> d.clear()
# >>> print d
# deque([])
# >>> d.extend('1')
# >>> print d
# deque(['1'])
# >>> d.extendleft('234')
# >>> print d
# deque(['4', '3', '2', '1'])
# >>> d.count('1')
# 1
# >>> d.pop()
# '1'
# >>> print d
# deque(['4', '3', '2'])
# >>> d.popleft()
# '4'
# >>> print d
# deque(['3', '2'])
# >>> d.extend('7896')
# >>> print d
# deque(['3', '2', '7', '8', '9', '6'])
# >>> d.remove('2')
# >>> print d
# deque(['3', '7', '8', '9', '6'])
# >>> d.reverse()
# >>> print d
# deque(['6', '9', '8', '7', '3'])
# >>> d.rotate(3)
# >>> print d
# deque(['8', '7', '3', '6', '9'])

# Code - 
d=deque()
for _ in range(int(input())):
    z=input().split()
    if z[0] == 'append':
        d.append(z[1])
    elif z[0] == 'appendleft':
        d.appendleft(z[1])
    elif z[0] == 'pop':
        d.pop()
    elif z[0] == 'popleft':
        d.popleft()
print(*d)
