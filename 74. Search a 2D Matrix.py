# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        """
        Efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
            - Integers in each row are sorted from left to right.
            - The first integer of each row is greater than the last integer of the previous row.
        """
        if not len(matrix):
            return False
    
        row, colum = 0, len(matrix[0]) - 1
        while row < len(matrix) and colum >= 0:
            matrixItem = matrix[row][colum]
            print(matrixItem)
            if matrixItem < target:
                row += 1
            elif matrixItem > target:
                colum -= 1
            else:
                return True
        return False
