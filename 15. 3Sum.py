# O(n^2) time | O(n) space
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        numsLen = len(nums)
        for i in range(numsLen - 2):
            left = i + 1
            right = numsLen - 1
            while left < right:
                currentSum = nums[i] + nums[left] + nums[right]
                if currentSum == 0:
                    triplets.add(tuple(sorted([nums[i], nums[left], nums[right]])))   
                    left += 1; right -= 1
                elif currentSum > 0:
                    right -= 1
                else:
                    left += 1
        return [[x[0], x[1], x[2]] for x in triplets]