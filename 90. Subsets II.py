# 90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: [int]) -> [[int]]:
        """
        Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
        """
        subsets = [[]]
        for num in sorted(nums):
            for index in range(len(subsets)):
                newSubset = subsets[index] + [num]
                if newSubset not in subsets:
                    subsets.append(newSubset)
        return subsets

