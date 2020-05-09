# 200. Number of Islands

class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        """
        Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
        An island is surrounded by water and is formed by connecting adjacent 
        lands horizontally or vertically. You may assume all four edges 
        of the grid are all surrounded by water.
        """
        islandsCount = [0]
        visited = [[False for _ in row] for row in grid]
        for row in range(len(grid)):
            for colum in range(len(grid[row])):
                if visited[row][colum]:
                    continue
                self.traverseNone(row, colum, grid, visited, islandsCount)
        return islandsCount[0]
                
    def traverseNone(self, row, colum, grid, visited, islandsCount):
        isIslandFound = False
        nodesToExplore = [[row, colum]]
        while len(nodesToExplore):
            currentRow, currentColum = nodesToExplore.pop()
            currentValue = grid[currentRow][currentColum]
            if visited[currentRow][currentColum]:
                continue
            visited[currentRow][currentColum] = True
            if currentValue == '0':
                continue
            isIslandFound = True
            unvisitedNeighbors = self.getUnvisitedNeighbors(currentRow, currentColum, grid, visited)
            for neighbor in unvisitedNeighbors:
                nodesToExplore.append(neighbor)
        if isIslandFound:
            islandsCount[0] += 1
            
    def getUnvisitedNeighbors(self, row, colum, grid, visited):
        unvisitedNeighbors = []
        if len(grid) > row + 1 and not visited[row + 1][colum]:
            unvisitedNeighbors.append([row + 1, colum])
        if len(grid[row]) > colum + 1 and not visited[row][colum + 1]:
            unvisitedNeighbors.append([row, colum + 1])
        if row > 0 and not visited[row - 1][colum]:
            unvisitedNeighbors.append([row - 1, colum])
        if colum > 0 and not visited[row][colum - 1] :
            unvisitedNeighbors.append([row, colum - 1])
        return unvisitedNeighbors
