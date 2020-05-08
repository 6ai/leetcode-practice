# 54. Spiral Matrix
# O(n) time | O(n) space
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        """
        Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
        Input:
                [
                 [ 1, 2, 3 ],
                 [ 4, 5, 6 ],
                 [ 7, 8, 9 ]
                ]
        Output: [1,2,3,6,9,8,7,4,5]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0: 
            return []
        startRow = startColum = 0
        endRow, endColum = len(matrix) - 1, len(matrix[0]) - 1
        result = []
        while startRow <= endRow and startColum <= endColum:
            for item in matrix[startRow][startColum : endColum + 1]:
                result.append(item)
            for row in range(startRow + 1, endRow + 1):
                result.append(matrix[row][endColum])
            if startRow != endRow:
                for item in reversed(matrix[endRow][startColum : endColum]):
                    result.append(item) 
            if startColum != endColum:
                for row in reversed(range(startRow + 1, endRow)):
                    result.append(matrix[row][startColum])
            startRow += 1; startColum += 1
            endRow -= 1; endColum -= 1
        return result
