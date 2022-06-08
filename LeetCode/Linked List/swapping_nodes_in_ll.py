'''
Link - https://leetcode.com/problems/swapping-nodes-in-a-linked-list/\


1721. Swapping Nodes in a Linked List
Medium

2813

107

Add to List

Share
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def length(self,head):
            count=0
            current_node1 = head
            while current_node1 is not None:
                count+=1
                current_node1 = current_node1.next
            return count
        swap_node_index = length(self,head) - k + 1
        current_node = head
        indexed_node = head
        count=1
        if k<swap_node_index:
            while current_node is not None:
                if count==k:
                    indexed_node = current_node
                if count==swap_node_index:
                    val = indexed_node.val
                    indexed_node.val = current_node.val
                    current_node.val = val
                    return head
                count+=1
                current_node = current_node.next
        elif k>swap_node_index:
            while current_node is not None:
                if count==swap_node_index:
                    indexed_node = current_node
                if count==k:
                    val = indexed_node.val
                    indexed_node.val = current_node.val
                    current_node.val = val
                    return head
                count+=1
                current_node = current_node.next
        return head
            