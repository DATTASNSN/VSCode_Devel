'''
Link - https://leetcode.com/problems/reverse-linked-list/submissions/

206. Reverse Linked List
Easy

12224

212

Add to List

Share
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []


'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current_node = head
        prev= None
        while current_node is not None:
            next = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next
        head = prev
        return head
        
        