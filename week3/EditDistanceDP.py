from collections import Counter
'''
  formula: if string1[i] == string2[j], table entry = left diagonal
  else: table entry = 1 +  min(left diagonal(replace?), left(delete?), top(insert?) )

  '' a b c d e f
'' 0 1 2 3 4 5 6
a  1 0 1 2 3 4 5
z  2 1 1 2 3 4 5
c  3 2 2 1 2
e  4
d  5
'''
class Solution:
    #recursive version
    def __init__(self):
        self.memo = dict()
    def minDistance(self, word1: str, word2: str) -> int:
        #call for recursive version
        # return self.distance(word1,word2,len(word1),len(word2))
        
        
        #dynamic programming version
        #add one to each range to account for empty string entry in table
        for i in range(len(word1)+1):
            for j in range(len(word2)+1):
                # print(i,j)
                if i == 0:
                    self.memo[(i,j)] = j 
                elif j == 0:
                    self.memo[(i,j)] = i
                
                elif word1[i-1] == word2[j-1]:
                    self.memo[(i,j)] = self.memo[(i-1,j-1)]
                
                else:
                    insert = self.memo[(i, j-1)]
                    remove = self.memo[(i-1, j)]
                    replace = self.memo[(i-1, j-1)]
                    self.memo[(i,j)] = 1 + min(insert,remove,replace)
                    
        # print(word1[-1])
        # print(self.memo)
        # print(self.memo[(len(word1),len(word2))])
        return self.memo[(len(word1),len(word2))]
                    
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    



