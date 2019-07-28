class Solution:
    def __init__(self):
        self.columns = None
        self.rows = None
        self.grid = None
        self.visited = set()
        self.ans = 0 
    def traverse(self,row,col):
        # print("grid [",row,"]","[",col,"] ")
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            # print("+1 out of bounds")			
            self.ans+=1
        elif self.grid[row][col] == 0:
            # print("+1 for 0")
            self.ans+=1
        elif (row,col) in self.visited:
            # print("already visited")
            pass
        elif (row,col) not in self.visited:
            self.visited.add((row,col))
            # print("left: ")
            self.traverse(row,col-1) # left
            # print("right: ")
            self.traverse(row,col+1) # right
            # print("up: ")
            self.traverse(row-1,col) # up 
            # print("down: ")
            self.traverse(row+1,col) # down
        
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid
        
        # print(self.rows,self.columns)
        
        for row in range(self.rows):
            for col in range(self.columns):
                if grid[row][col] == 1:
                    self.traverse(row,col)
                    return self.ans