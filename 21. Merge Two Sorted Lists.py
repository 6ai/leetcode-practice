# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
    
        rootNode = None
        if l1.val < l2.val:
            rootNode = l1
            l1 = l1.next
        else:
            rootNode = l2
            l2 = l2.next
        
        currentNode = rootNode
        while (l1 != None) and (l2 != None):
            if l1.val > l2.val:
                currentNode.next = l2
                l2 = l2.next
            else:
                currentNode.next = l1
                l1 = l1.next
            currentNode = currentNode.next
        currentNode.next = l1 if (l1 != None) else l2
        return rootNode