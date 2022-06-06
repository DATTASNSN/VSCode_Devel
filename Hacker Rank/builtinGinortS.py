  # https://www.hackerrank.com/challenges/ginorts/problem

# Input Format

# A single line of input contains the string s.

# Output Format

# Output the sorted string .

# Sample Input

# Sorting1234

# Sample Output

# ginortS1324

# Code -

order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1357902468'
print(*sorted(input(), key=order.index), sep='')
