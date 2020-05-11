# 78. Subsets

class Solution:
    def subsets(self, nums: [int]) -> [[int]]:
        subsets = [[]]
        for num in nums:
            for index in range(len(subsets)):
                newSubset = subsets[index] + [num]
                subsets.append(newSubset)
        return subsets        
        