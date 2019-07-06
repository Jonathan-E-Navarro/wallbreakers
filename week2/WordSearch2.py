class TrieNode():
    def __init__(self):
        #children is dictionary that contains trie nodes 
        self.children = collections.defaultdict(TrieNode)
        #if isword = true, it marks the end of a word in the chain 
        self.isWord = False
    
class Trie():
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for w in word:
            node = node.children[w]
        node.isWord = True
    
    def search(self, word):
        node = self.root
        for w in word:
            node = node.children.get(w)
            if not node:
                return False
        return node.isWord
class Solution(object):
    def findWords(self, board, words):
        print(board)
        print(words)
        
        solution = []
        trie = Trie()
        node = trie.root
        
        #insert all of our words into the trie 
        #we use the trie to track our progess in the DFS 
        for word in words:
            trie.insert(word)
            
        for row in range(len(board)):
            for col in range(len(board[0])):
                #start DFS
                self.dfs(row,col,board,solution,node,"")
        return solution
        
    '''
    DFS takes in col,row,board,node and path 
    row = sublist 
    col = index in particular sublist 
    board[row][col] = char
    node is a trie list node, we use these to track our progress in the DFS 
    path is the string we build to add to our result list
    '''
    def dfs(self,row,col,board,result,node,path):
        #if true, then our trie has marked the end of word for our current path 
        if node.isWord:
            result.append(path)
            #we set isword to false after so that we can find words that our current word is a substring of
            node.isWord = False
             
        #check if indexes are out of bounds 
        if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]):
            return 
        
        #copy current letter to temp and update board place to #
        temp = board[row][col]
        #we set our new node to be the child of our current letter, so we can keep track of DFS
        node = node.children.get(temp)
        if not node:
            return
        
        #set our current place in the board to placeholder so that 
        #backing cases dont mistake a used character as a valid path : [['a','a'],[,'a','b']] "baaab"
        board[row][col] = '#'
        #check every direction 
        self.dfs(row+1,col,board,result,node,path+temp) 
        self.dfs(row-1,col,board,result,node,path+temp) 
        self.dfs(row,col+1,board,result,node,path+temp) 
        self.dfs(row,col-1,board,result,node,path+temp)
        board[row][col] = temp