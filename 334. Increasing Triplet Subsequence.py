# 334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: [int]) -> bool:
        """
        Return true if there exists i, j, k 
        such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False     