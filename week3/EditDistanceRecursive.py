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
    def distance(self,word1,word2,m,n):
        if (m,n) in self.memo:
            return self.memo[(m,n)]
        if m == 0:
            return n
        if n == 0:
            return m 
        
        if word1[m-1] == word2[n-1]:
            sub = self.distance(word1,word2,m-1,n-1)
            self.memo[(m-1,n-1)] = sub 
            return sub
        
        insert = self.distance(word1, word2, m, n-1)
        remove = self.distance(word1, word2, m-1, n)
        replace = self.distance(word1, word2, m-1, n-1) 
        self.memo[(m, n-1)] = insert
        self.memo[(m-1,n)] = remove
        self.memo[(m-1, n-1)] = replace 
        
        return 1 + min(insert,remove,replace)
    
    def minDistance(self, word1: str, word2: str) -> int:
        #call for recursive version
        return self.distance(word1,word2,len(word1),len(word2))