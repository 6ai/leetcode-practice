class Solution:
    def fourSum(self, nums: [int], target: int) -> [[int]]:
        """
        Given an array nums of n integers and an integer target,
        are there elements a, b, c, and d in nums such that a + b + c + d = target?
        Find all unique quadruplets in the array which gives the sum of target.
        """
        allPairSums = dict()
        quadruplets = set()
        for i in range(1, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                currentPair = [nums[i], nums[j]]
                currentSum = sum(currentPair)
                diff = target - currentSum
                if diff in allPairSums:
                    for pair in allPairSums[diff]:
                        quadruplets.add(tuple(sorted(currentPair + pair)))
            for k in range(i):
                currentPair = [nums[i], nums[k]]
                currentSum = sum(currentPair)
                if currentSum not in allPairSums:
                    allPairSums[currentSum] = [currentPair]
                else:
                    allPairSums[currentSum].append(currentPair)
        return quadruplets

