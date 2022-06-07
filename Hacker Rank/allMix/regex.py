# https://www.hackerrank.com/challenges/re-group-groups/problem

# group()
# A group() expression returns one or more subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.group(0)       # The entire match 
# 'username@hackerrank.com'
# >>> m.group(1)       # The first parenthesized subgroup.
# 'username'
# >>> m.group(2)       # The second parenthesized subgroup.
# 'hackerrank'
# >>> m.group(3)       # The third parenthesized subgroup.
# 'com'
# >>> m.group(1,2,3)   # Multiple arguments give us a tuple.
# ('username', 'hackerrank', 'com')
# groups()
# A groups() expression returns a tuple containing all the subgroups of the match.
# Code

# >>> import re
# >>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
# >>> m.groups()
# ('username', 'hackerrank', 'com')
# groupdict()
# A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name.
# Code

# >>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
# >>> m.groupdict()
# {'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}




# Problem -- 

# Input Format

# A single line of input containing the string .

# Constraints


# Output Format

# Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

# Sample Input

# ..12345678910111213141516171820212223
# Sample Output

# 1
# Explanation

# .. is the first repeating character, but it is not alphanumeric.
# 1 is the first (from left to right) alphanumeric repeating character of the string in the substring 111.

# Code - 

import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)
# My solution has an even shorter regex, but I wrote it only for fun and I'd suggest not to use it to solve such a simple problem:

# (\w(?!_))\1+


# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
# Validating Email with Regex Filter.
import re
def fun(s):
    # return True if s is a valid email, else return False
    pattern = "^[a-zA-z0-9_-]+\@[a-zA-Z0-9]+\.\w?\w?\w?$"
    
    if re.search(pattern,s):
        # c=s.index('.')
        # if len(s[c+1:])<=3 and s.count('@')==1:
        #     return True
        # else:
        #     return False
        return True
    else:
        return False
def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)  