'''
https://leetcode.com/problems/reverse-linked-list-ii/


92. Reverse Linked List II
Medium

6524

306

Add to List

Share
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the list from position left to position right, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from tkinter.tix import ListNoteBook
from typing import Optional


class Solution:
    def reverseBetween(self, head: Optional[ListNoteBook], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        dummy = ListNode(0, next = head)
        prev, step = dummy, 1
        while step < left:
            prev = prev.next
            step += 1
        # We have found the prev node before left
        cur = prev.next
        nxt = cur.next 
        while step < right:
            save_nxt = nxt.next
            nxt.next = cur # reverse linked list
            cur = nxt 
            nxt = save_nxt
            step += 1
        prev.next.next = nxt
        prev.next = cur
        return dummy.next
        # My Code
        # count = 1
        # current_node = head
        # replace_node = ListNode()
        # return_node = replace_node
        # prev = None
        # flag = False
        # while current_node is not None:
        #     while count >= left and count <= right:
        #         next_node = current_node.next
        #         current_node.next = prev
        #         prev = current_node
        #         count+=1
        #         flag = True
        #         current_node = next_node
        #         print(current_node)
        #     if flag==True:
        #         replace_node.next = prev
        #         print(replace_node)
        #         while replace_node.next is not None:
        #             replace_node = replace_node.next
        #         replace_node.next = current_node
        #         return return_node.next
        #     replace_node.next = current_node
        #     replace_node = replace_node.next
        #     count+=1
        #     current_node = current_node.next
        # return head