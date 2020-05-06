# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import copy

class Solution:
    def calcSum(self, array: List[int]) -> int:
        result = 0
        for x in array:
            result += x
        return result

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        rootSums = []
        self.depthFirstSearch(root, [], rootSums)

        return [rootSum for rootSum in rootSums if self.calcSum(rootSum) == sum]

    def depthFirstSearch(self, treeNode: TreeNode, runnigSum: List[int], sums: List[List[int]]) -> None:
        if treeNode is None: return
        runnigSum.append(treeNode.val)
        if treeNode.left is None and treeNode.right is None:
            sums.append(runnigSum)
            return
        
        self.depthFirstSearch(treeNode.left, copy.deepcopy(runnigSum), sums)
        self.depthFirstSearch(treeNode.right, copy.deepcopy(runnigSum), sums)

    