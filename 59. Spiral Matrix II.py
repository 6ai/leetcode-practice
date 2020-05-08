# 59. Spiral Matrix II

# O(n) time | O(n) space
class Solution:
    def fillMatrix(self, spiralMatrix: [[int]], startIter: int, endIter: int, runningValue=1) -> None:
        if startIter > endIter:
            return
        
        for index in range(startIter, endIter + 1):
            spiralMatrix[startIter][index] = runningValue
            runningValue += 1
        for index in range(startIter + 1, endIter + 1):
            spiralMatrix[index][endIter] = runningValue
            runningValue += 1
        for index in reversed(range(startIter, endIter)):
            spiralMatrix[endIter][index] = runningValue 
            runningValue += 1
        for index in reversed(range(startIter + 1, endIter)):
            spiralMatrix[index][startIter] = runningValue 
            runningValue += 1
        self.fillMatrix(spiralMatrix, startIter + 1, endIter - 1, runningValue)

    def generateMatrix(self, n: int) -> [[int]]:
        """
        Given a positive integer n, generate a square matrix filled with elements from 1 to n^2 in spiral order.
        """
        matrix = [[None for _ in range(n)] for _ in range(n)]
        self.fillMatrix(matrix, 0, n - 1)
        print(matrix)
        return matrix
        