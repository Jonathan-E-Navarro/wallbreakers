import sys
class Solution:
    def __init__(self):
        self.path = 0 
        self.matrix = None
        self.visited = []
        self.memo = None
        self.directions = [(1,0),(-1,0),(0,1),(0,-1)]
        
    def dfs(self,row,col):
        if not self.memo[row][col]:
            for d in self.directions:
                if row+d[0]>=0 and row+d[0]<self.rows and col+d[1]>=0 and col+d[1]<self.columns and self.matrix[row+d[0]][col+d[1]]>self.matrix[row][col]:
                    self.memo[row][col] =  max(self.memo[row][col],self.dfs(row+d[0],col+d[1]))
            self.memo[row][col]+=1
        return self.memo[row][col]
        
    
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: 
            return 0
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self.memo = [[0]*self.columns for _ in range(self.rows)]
        
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                # print("dfs:")
                self.path = max(self.path,self.dfs(row,col))
        return self.path
        