class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        #dfs is going to modify every O that can be reached by another O
        def dfs(row, col):
            # if not within boundary or on boundary or not a zero, return
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                # print("returning")
                return 
            if board[row][col] != 'O':
                return
            # changed every 0 that can be touched by a DFS to a *     
            board[row][col] = '*'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        #iterate through board and call DFS when appropriate    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row in {0, len(board)-1} or col in {0, len(board[0])-1} and board[row][col] == 'O':
                    dfs(row,col)    
            
        #every O seen at this point could not be reached through another O so its a surrounded region, flip it to x             #every * can be flipped back to a 0 since it was not surrounded by X's
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == '*':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'

"""
Thought process:
We are going to perform a DFS,
Our dfs is going to modify every O that can be reached by another O
if not within boundary or on boundary or not a zero, return
changed every 0 that can be touched by a DFS to a *     
iterate through board and call DFS when appropriate    
every O seen at this point could not be reached through another O 
so its a surrounded region, flip it to x            
every * can be flipped back to a 0 since it was not surrounded by X's


"""