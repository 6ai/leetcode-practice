# 240. Search a 2D Matrix II

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        Efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
            - Integers in each row are sorted in ascending from left to right.
            - Integers in each column are sorted in ascending from top to bottom.
        """
        if not len(matrix):
            return False
    
        row, colum = 0, len(matrix[0]) - 1
        while row < len(matrix) and colum >= 0:
            matrixItem = matrix[row][colum]
            if matrixItem < target:
                row += 1
            elif matrixItem > target:
                colum -= 1
            else:
                return True
        return False
