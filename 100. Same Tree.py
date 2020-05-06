# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthFirthSearch(self, treeNode: TreeNode, array: [int]) -> None:
        if treeNode is None:
            array.append(None)
            return
        array.append(treeNode.val)
        
        self.depthFirthSearch(treeNode.left, array)
        self.depthFirthSearch(treeNode.right, array)

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pTreeNodesValues = []
        self.depthFirthSearch(p, pTreeNodesValues)
        qTreeNodesValues = []
        self.depthFirthSearch(q, qTreeNodesValues)
        return qTreeNodesValues == pTreeNodesValues

