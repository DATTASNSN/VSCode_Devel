# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

# Sample Input

# rabcdeefgyYhFjkIoomnpOeorteeeeet
# Sample Output

# ee
# Ioo
# Oeo
# eeeee
# Explanation

# ee is located between consonant  d and f.
# Ioo is located between consonant k and m.
# Oeo is located between consonant p and r.
# eeeee is located between consonant t and t.

# # Enter your code here. Read input from STDIN. Print output to STDOUT
# import re
# s=input()
# print(list(map(lambda x:x.group(),re.finditer(r'aeiouAeiou',s))))
import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)
if match:
    for i in match:
        print(i)
else:
    print(-1)
