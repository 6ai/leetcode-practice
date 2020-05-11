# 46. Permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of distinct integers, return all possible permutations.
        """
        permutations = []
        self.helper(nums, [], permutations)
        return permutations
        
    def helper(self, array, currentPermutation, permutations):
        if not len(array) and len(currentPermutation):
            permutations.append(currentPermutation)
        else:
            for index in range(len(array)):
                newArray = array[: index] + array[index + 1:]
                newPermutation = currentPermutation + [array[index]]
                self.helper(newArray, newPermutation, permutations)
