'''
https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-three

Sample Input

11
middle-Outz
2
Sample Output

okffng-Qwvb
Explanation

Original alphabet:      abcdefghijklmnopqrstuvwxyz
Alphabet rotated +2:    cdefghijklmnopqrstuvwxyzab

m -> o
i -> k
d -> f
d -> f
l -> n
e -> g
-    -
O -> Q
u -> w
t -> v
z -> b

Code- 

!/bin/python3
'''

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s,k):
  k = k % 26
  z=''
  for i in s:
      if i.isalpha():
        if i.isupper():
          if ord(i)+k>90:
            z+=chr(ord(i)+k-26)
          else:
            z+=chr(ord(i)+k)
        if i.islower():
          if ord(i)+k>122:
            z+=chr(ord(i)+k-26)
          else:
            z+=chr(ord(i)+k)
      else:
        z+=i
  return z
if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  s = input()

  k = int(input().strip())

  result = caesarCipher(s, k)

  fptr.write(result + '\n')

  fptr.close()
