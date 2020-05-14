# 203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head is not None and head.val == val:
            head = head.next
        currentNode = head
        prevNode = head
        while currentNode is not None:
            currentNode = currentNode.next
            while currentNode is not None and currentNode.val == val:
                currentNode = currentNode.next
            prevNode.next = currentNode
            prevNode = prevNode.next
            
        return head