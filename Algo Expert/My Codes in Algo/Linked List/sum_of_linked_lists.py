# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
  current_node_one = linkedListOne
  current_node_two = linkedListTwo
  temp_one = ''
  temp_two = ''
  while current_node_one is not None:
    temp_one += str(current_node_one.value)
    current_node_one = current_node_one.next
  while current_node_two is not None:
    temp_two += str(current_node_two.value)
    current_node_two = current_node_two.next
  result = str(int(temp_one[::-1]) + int(temp_two[::-1]))[::-1]
  new_ll = LinkedList(0)
  current_node = new_ll
  i=0
  while i<len(result):
    new_node = LinkedList(int(result[i]))
    current_node.next = new_node
    current_node = new_node
    i+=1
  return new_ll.next
