class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for idxOne in range(len(nums) - 1):
            if nums[idxOne] != 0:
                continue
            idxTwo = idxOne + 1
            while nums[idxTwo] == 0 and idxTwo < (len(nums) - 1):
                idxTwo += 1
            nums[idxOne], nums[idxTwo] = nums[idxTwo], nums[idxOne]