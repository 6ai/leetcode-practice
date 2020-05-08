# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getBSTNodeValues(self, root: TreeNode, runnigSum: int, l: int, r: int) -> None:
        if root is None:
            return 
        if root.val < l:
            self.getBSTNodeValues(root.right, runnigSum, l, r)
        elif root.val > r:
            self.getBSTNodeValues(root.left, runnigSum, l, r)
        else:
            runnigSum[0] += root.val
            self.getBSTNodeValues(root.right, runnigSum, l, r)
            self.getBSTNodeValues(root.left, runnigSum, l, r)            
            
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        runnigSum = [0]
        self.getBSTNodeValues(root, runnigSum, L, R)
        return runnigSum[0]