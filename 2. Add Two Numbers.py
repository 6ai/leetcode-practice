# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def listNodeToInteger(self, l: ListNode) -> int:
        integer = l.val; x = 1
        while l.next is not None:
            x *= 10
            l = l.next
            integer += l.val * x 
        return integer
    
    def integerToListNode(self, integer: int) -> ListNode:
        rootNode = ListNode(integer % 10)
        currentNode = rootNode
        integer //= 10
        while integer > 0:
            currentNode.next = ListNode(integer % 10)
            currentNode = currentNode.next
            integer //= 10
        return rootNode
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return self.integerToListNode(self.listNodeToInteger(l1) + self.listNodeToInteger(l2))