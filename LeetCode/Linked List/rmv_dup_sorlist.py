'''
Link - https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/ 

(I)

83. Remove Duplicates from Sorted List
Easy

4974

189

Add to List

Share
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,1,2]
Output: [1,2]
Example 2:


Input: head = [1,1,2,3,3]
Output: [1,2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dup = []
        current_node= head
        while current_node is not None:
            if current_node.val not in dup:
                dup.append(current_node.val)
                previous_node = current_node
            elif current_node.val in dup:
                previous_node.next = current_node.next
                current_node = previous_node
            current_node = current_node.next
        return head


'''
Link - https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

II - 

82. Remove Duplicates from Sorted List II
Medium

5877

173

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        current_node = head
        dup = set([])
        if current_node.next is not None and head.val == current_node.next.val:
            head = head.next
            current_node = current_node.next
            dup.add(head.val)
        previous_node = head
        while current_node.next is not None:
            if current_node.val in dup:
                previous_node.next = current_node.next
                current_node = previous_node
            if current_node.val == current_node.next.val:
                dup.add(current_node.val)
                previous_node.next = current_node.next
                current_node = previous_node
            previous_node = current_node
            current_node = current_node.next
        if current_node.val in dup:
            previous_node.next = None
        if head.val in dup:
            return head.next
        return head
        