# https://leetcode.com/problems/add-two-numbers/submissions/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        nom_l1 = ''
        nom_l2 = ''
        current_node1 = l1
        current_node2 = l2
        while current_node1:
            nom_l1+=str(current_node1.val)
            current_node1 = current_node1.next
        while current_node2:
            nom_l2+=str(current_node2.val)
            current_node2 = current_node2.next
        res = str(int(nom_l1[::-1]) + int(nom_l2[::-1]))[::-1]
        result = ListNode(0)
        main = result
        for i in range(len(res)):
            new_node = ListNode(res[i])
            main.next = new_node
            main = main.next
        return result.next
        