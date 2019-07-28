class Solution(object):
    def __init__(self):
        self.word = None
        self.index = 0 
    def exist(self, board, word):
        '''
        we're going to do a DFS, and the path whose existence we're going to check is actually our word 
        ''' 
        self.word = word
        for row in range(len(board)):
            for col in range(len(board[0])):
                char = board[row][col]
                #check if we can start our DFS
                if char == word[0]:
                    #start DFS
                    # if self.dfs(row,col,word,board):
                    #     return True
                    if self.dfs2(row,col,0,board):
                        return True
                    
        return False
    def dfs(self,row,col,word,board):
        #check if all characters have been checked
        if len(word) == 0:
            return True
        #check if indexes are out of bounds 
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or word[0]!=board[row][col]:
            return False
        #copy current letter to temp and update board place to 0 
        temp = board[row][col]
        #edit this char to avoid counting it again
        board[row][col] = '*'
        #check every direction 
        result = self.dfs(row+1,col,word[1:],board) \
        or self.dfs(row-1,col,word[1:],board) \
        or self.dfs(row,col+1,word[1:],board) \
        or self.dfs(row,col-1,word[1:],board)
        #put original character back 
        board[row][col] = temp
        return result
    
    
    def dfs2(self,row,col,index,board):
        #check if all characters have been checked
        if index == len(self.word):
            return True
        #check if indexes are out of bounds 
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or self.word[index]!=board[row][col]:
            return False
        #copy current letter to temp and update board place to 0 
        temp = board[row][col]
        #edit this char to avoid counting it again
        board[row][col] = '*'
        #check every direction 
        result = self.dfs2(row+1,col,index+1,board) \
        or self.dfs2(row-1,col,index+1,board) \
        or self.dfs2(row,col+1,index+1,board) \
        or self.dfs2(row,col-1,index+1,board)
        #put original character back 
        board[row][col] = temp
        return result

                    

              