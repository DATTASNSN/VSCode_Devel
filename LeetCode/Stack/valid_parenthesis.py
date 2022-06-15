'''
Link - https://leetcode.com/problems/valid-parentheses/

20. Valid Parentheses
Easy

13555

613

Add to List

Share
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        for x in range(len(s)//2):
            s = s.replace('()', '').replace('{}', '').replace('[]', '')
        return len(s) == 0