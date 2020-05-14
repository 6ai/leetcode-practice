# 27. Remove Element
    
class Solution:
    """
    Given an array nums and a value val, remove all instances of that value in-place and return the new length.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        while index < len(nums):
            if nums[index] == val:
                nums.pop(index)
            else:
                index += 1
        return len(nums)
        
        