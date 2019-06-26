class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(row, col):
            # print(not 0 <= row < len(board))
            if not 0 <= row < len(board) or not 0 <= col < len(board[0]) or board[row][col] != 'O':
                return 
            board[row][col] = 'D'
            dfs(row+1, col)
            dfs(row-1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                if row in {0, len(board)-1} or col in {0, len(board[0])-1} and board[row][col] == 'O':
                    dfs(row,col)    
                    
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == 'D':
                    board[row][col] = 'O'
                elif board[row][col] == 'O':
                    board[row][col] = 'X'
                    
                    
                    
        