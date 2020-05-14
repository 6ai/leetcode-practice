# 62. Unique Paths

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        paths = [[(0 if k > 0 and i > 0 else 1) for i in range(m)] for k in range(n)]
        
        for col in range(1, m):
            for row in range(1, n):
                if row > 0:
                    paths[row][col] += paths[row - 1][col]
                if col > 0:
                    paths[row][col] += paths[row][col - 1]
                    
        return paths[-1][-1]
        