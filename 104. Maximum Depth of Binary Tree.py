# 104. Maximum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def depthFirstSearch(self, treeNode: TreeNode, runnigDepth: int,
                         currentMaxPath2Leaf: [int]) -> None:
        if treeNode is None: return
        if treeNode.left is None and treeNode.right is None:
            currentMaxPath2Leaf[0] = max(currentMaxPath2Leaf[0], runnigDepth)
        
        runnigDepth += 1
        
        self.depthFirstSearch(treeNode.left, runnigDepth, currentMaxPath2Leaf)
        self.depthFirstSearch(treeNode.right, runnigDepth, currentMaxPath2Leaf)

    def maxDepth(self, root: TreeNode) -> int:
        if root is None: return 0
        maxDepthPath = [1]
        self.depthFirstSearch(root, 1, maxDepthPath)
        return maxDepthPath[0]
    