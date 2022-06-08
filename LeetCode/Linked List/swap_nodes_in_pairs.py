'''
Link - https://leetcode.com/problems/swap-nodes-in-pairs/

24. Swap Nodes in Pairs
Medium

7119

297

Add to List

Share
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def length(self,head):
            count=0
            current_node1 = head
            while current_node1 is not None:
                count+=1
                current_node1 = current_node1.next
            return count
        pairLength = length(self,head)
        current_node = head
        if pairLength%2==0:
            while current_node is not None:
                val = current_node.val
                current_node.val = current_node.next.val
                current_node.next.val = val
                current_node = current_node.next.next
        else:
            while current_node is not None: 
                if pairLength==1:
                    return head
                pairLength-=2
                val = current_node.val
                current_node.val = current_node.next.val
                current_node.next.val = val
                current_node = current_node.next.next
        return head