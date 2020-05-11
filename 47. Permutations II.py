# 47. Permutations II

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        Given a collection of numbers that might contain duplicates, return all possible unique permutations.
        """
        permutations = set()
        self.helper(nums, [], permutations)
        return permutations
        
    def helper(self, array, currentPermutation, permutations):
        if not len(array) and len(currentPermutation):
            permutations.add(tuple(currentPermutation))
        else:
            for index in range(len(array)):
                newArray = array[: index] + array[index + 1:]
                newPermutation = currentPermutation + [array[index]]
                self.helper(newArray, newPermutation, permutations)
