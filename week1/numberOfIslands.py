class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        #if empty 
        if len(grid) == 0: 
            return 0
        #visited matrix for DFS 
        visited = [[0 for col in range(len(grid[0]))] for row in range(len(grid))]

        def dfs(row, col):
            #if out of bounds 
            if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
                return False
            #if water or piece of land that's been visited
            if grid[row][col] == '0' or visited[row][col]:
                return False
            #mark as visited
            visited[row][col] = 1 
            #DFS in every direction
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            return True
        
        #iterate through grid For each, DFS call finished, an island has been searched
        count = 0 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                    if dfs(row,col):
                        count += 1
        return count
        