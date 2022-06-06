'''
5. Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"

Link - https://leetcode.com/problems/longest-palindromic-substring/
'''


class Solution:
  def longestPalindrome(self, s: str) -> str:
    res="" 
    for k in range(len(s)):  
      res = max(self.helper(s,k,k), self.helper(s,k,k+1), res, key=len)
  #     tmp1 = self.helper(s,k,k)
  #     tmp2 = self.helper(s,k,k+1)
  #    if len(tmp1)>max: res = tmp1  
  #    if len(tmp2)>max: res = tmp2  
    return res


  def helper(self, s, i, j):
    while i>=0 and j<len(s) and s[i] == s[j]:
      i -= 1
      j +=1
    return s[i+1:j]                