'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         def removing_index(self,head: Optional[ListNode],n) -> int:
#             current_node = head
#             length = 0
#             while current_node:
#                 length+=1
#                 current_node = current_node.next
#             return length
#         if removing_index(self,head,n)==1 and n==1:
#             return head.next
#         n = removing_index(self,head,n) - n
#         current_node = head
#         previous_node = head
#         while n==0:
#             return current_node.next
#         while n!=0:
#             previous_node = current_node
#             current_node = current_node.next
#             n-=1
#         previous_node.next = current_node.next
#         return head