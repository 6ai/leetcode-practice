class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsHashTable = dict([(key, value) for value, key in enumerate(nums)])
        for i in range(len(nums)):
            interimSum = targlet - nums[i]
            if interimSum in numsHashTable:
                if numsHashTable[interimSum] != i:
                    return [i, numsHashTable[interimSum]]
        