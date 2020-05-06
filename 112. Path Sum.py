# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthFirstSearch(self, treeNode: TreeNode, runnigSum: int, sums: set) -> None:
        if treeNode is None: return
        runnigSum += treeNode.val
        if treeNode.left is None and treeNode.right is None:
            sums.add(runnigSum)
            return
        
        self.depthFirstSearch(treeNode.left, runnigSum, sums)
        self.depthFirstSearch(treeNode.right, runnigSum, sums)

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        rootSums = set()
        self.depthFirstSearch(root, 0, rootSums)
        return sum in rootSums