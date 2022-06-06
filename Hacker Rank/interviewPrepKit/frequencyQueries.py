# https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_r=next-challenge&h_v=zen&h_v=zen&h_v=zen&h_v=zen&isFullScreen=true&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

import math
import os
import random
import re
import sys
from collections import defaultdict
# Complete the freqQuery function below.
def freqQuery(queries):
  # Mycode -
    # z=[]
    # output=[]
    # for i in queries:
    #     if i[0]==1:
    #         z.append(i[1])
    #     elif i[0]==2:
    #         if i[1] in z:
    #             z.remove(i[1])
    #     elif i[0]==3:
    #         count=0
    #         for j in z:
    #             if z.count(j)==i[1]:
    #                 count+=1
    #                 output.append('1')
    #                 break
    #         if count==0:
    #             output.append('0')
    # return output
    # Less time complexity code -
    res = []
    fre = defaultdict(int)
    for x in queries:
      if x[0] == 1:
        fre[x[1]] += 1
      elif x[0] == 2:
        if x[1] in fre and fre[x[1]] > 0:
            fre[x[1]] -= 1
      else:
        res.append(1 if x[1] in set(fre.values()) else 0)
      print(fre)
    return res
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = 8

    queries = [[1,5],[1,6],[3,2],[1,10],[1,6],[2,5],[3,2]]

    # for _ in range(q):
    #     queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)
    print(ans)

    # fptr.write('\n'.join(map(str, ans)))
    # fptr.write('\n')

    # fptr.close()