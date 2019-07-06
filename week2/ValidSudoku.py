from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:                    
        #first we check rows 
        seen = defaultdict(int)
        for row in range(len(board)):
            seen.clear()
            for col in range(len(board[0])):
                if board[row][col]!= ".":
                    seen[board[row][col]]+=1
                    if(seen[board[row][col]]>1):
                        return False
        
        #Next we check colummns   
        for col in range(len(board[0])):
            seen.clear()
            for row in range(len(board)):
                if board[row][col]!= ".":
                    seen[board[row][col]]+=1
                    if(seen[board[row][col]]>1):
                        return False

        #last we check the boxes
        for i in range(0,9,3):
            for j in range(0,9,3):
                seen.clear()
                for x in range(3):
                    for y in range(3): 
                        if board[i+x][j+y] !='.':
                            seen[board[i+x][j+y]] +=1
                            if(seen[board[i+x][j+y]])>1:
                                return(False)
        return True
        
        