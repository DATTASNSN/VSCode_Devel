'''
Link - https://leetcode.com/problems/zigzag-conversion/

6. Zigzag Conversion
Medium

3750

8607

Add to List

Share
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"



'''

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        c= ['']*numRows
        count=0
        measure = len(s)
        measure2 = measure
        length=0
        while length <= measure-1:
            if count%2==0:
                for i in range(numRows):
                    if measure2>0:
                        c[i]+=s[length + i]
                        measure2-=1
                count+=1
                length+=numRows
            else:
                for i in range(1,numRows-2+1):
                    if measure2>0:
                        c[numRows-i-1]+=s[length]
                        measure2-=1
                        length+=1
                count+=1
        res = ''
        for j in c:
            res+=j
        return res
                    