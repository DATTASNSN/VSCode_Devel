# https://www.hackerrank.com/challenges/py-set-union/problem
# UNION
s = set("Hacker")
print(s.union("Rank"))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(set(['R', 'a', 'n', 'k'])))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(['R', 'a', 'n', 'k']))
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

print(s.union(enumerate(['R', 'a', 'n', 'k'])))
# set(['a', 'c', 'r', 'e', (1, 'a'), (2, 'n'), 'H', 'k', (3, 'k'), (0, 'R')])

print(s.union({"Rank":1}))
# set(['a', 'c', 'r', 'e', 'H', 'k', 'Rank'])

s | set("Rank")
# set(['a', 'R', 'c', 'r', 'e', 'H', 'k', 'n'])

# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(input().split())
m=int(input())
b=set(input().split())
print(len(a.union(b)))

# INTERSECTION
s = set("Hacker")
print(s.intersection("Rank"))
# set(['a', 'k'])

print(s.intersection(set(['R', 'a', 'n', 'k'])))
# set(['a', 'k'])

print(s.intersection(['R', 'a', 'n', 'k']))
# set(['a', 'k'])

print(s.intersection(enumerate(['R', 'a', 'n', 'k'])))
# set([])

print(s.intersection({"Rank":1}))
# set([])

s & set("Rank")
# set(['a', 'k'])

# Difference(A-B)
s = set("Hacker")
print(s.difference("Rank"))
# set(['c', 'r', 'e', 'H'])

print(s.difference(set(['R', 'a', 'n', 'k'])))
# set(['c', 'r', 'e', 'H'])


print(s.difference(['R', 'a', 'n', 'k']))
# set(['c', 'r', 'e', 'H'])

print(s.difference(enumerate(['R', 'a', 'n', 'k'])))
# set(['a', 'c', 'r', 'e', 'H', 'k'])

print(s.difference({"Rank":1}))
# set(['a', 'c', 'e', 'H', 'k', 'r'])

s - set("Rank")
# set(['H', 'c', 'r', 'e'])

# SymetricIntersection(A^B)
s = set("Hacker")
print(s.symmetric_difference("Rank"))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(set(['R', 'a', 'n', 'k'])))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(['R', 'a', 'n', 'k']))
# set(['c', 'e', 'H', 'n', 'R', 'r'])

print(s.symmetric_difference(enumerate(['R', 'a', 'n', 'k'])))
# set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

print(s.symmetric_difference({"Rank":1}))
# set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

s ^ set("Rank")
# set(['c', 'e', 'H', 'n', 'R', 'r'])

#IMPORTANT - Update of every function mutation two sets because we can use only above functions for the per-defined sets but there is any fetaure to update the sets of different functions b8ut there is no option of printing length when we are updating sets.
# unionUpdate
H = set("Hacker")
R = set("Rank")
H.update(R)
print(H)
# set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

# intersectionUpdate
H = set("Hacker")
R = set("Rank")
H.intersection_update(R)
print (H)
# set(['a', 'k'])

# differenceUpdate
H = set("Hacker")
R = set("Rank")
H.difference_update(R)
print(H)
# set(['c', 'e', 'H', 'r'])

# symetricDifferenceUpdate
H = set("Hacker")
R = set("Rank")
H.symmetric_difference_update(R)
print(H)
# set(['c', 'e', 'H', 'n', 'r', 'R'])
