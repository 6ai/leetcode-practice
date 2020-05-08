# 896. Monotonic Array
# O(n) time | O(1) space
class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        isIncreasing = True
        isDecreasing = True
        for index in range(1, len(A)):
            if A[index - 1] < A[index]:
                isDecreasing = False
            if A[index - 1] > A[index]:
                isIncreasing = False
        return isIncreasing or isDecreasing
        