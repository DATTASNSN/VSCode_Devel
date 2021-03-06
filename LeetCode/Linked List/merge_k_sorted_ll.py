'''
Link - https://leetcode.com/problems/merge-k-sorted-lists/

23. Merge k Sorted Lists
Hard

12427

482

Add to List

Share
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []



'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = []
        for lis in lists:
            current_node = lis
            while current_node is not None:
                res.append(current_node.val)
                current_node = current_node.next
        res = sorted(res)
        count=0
        new_node = ListNode(0)
        cre_node = new_node
        for i in res:
            node = ListNode(i)
            cre_node.next = node
            cre_node = cre_node.next
        return new_node.next