# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?h_r=next-challenge&h_v=zen

# Sample Input

# 2  
# DEXTER <dexter@hotmail.com>
# VIRUS <virus!@variable.:p>
# Sample Output

# DEXTER <dexter@hotmail.com>
# Explanation

# dexter@hotmail.com is a valid email address, so we print the name and email address pair received as input on a new line.
# virus!@variable.:p is not a valid email address because the username contains an exclamation point (!) and the extension contains a colon (:). As this email is not valid, we print nothing.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=re.compile(r'<[a-zA-Z]{1}[a-zA-Z0-9._-]+@[A-Za-z]+\.[A-Za-z]{1,3}>$')
for i in range(int(input())):
    s=input().split()
    if pattern.match(s[1]):
        print(*s)