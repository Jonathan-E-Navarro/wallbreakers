class UnionFind:
    def __init__(self, length):
        #initialize parents to be number of people (in case everyone is only friends with themselves they are their own parent)
        self.parents = [i for i in range(length)]
        #initalize friend group count to number of people in case everyone is only friends with themselves
        self.count = length
        
    #finds which parent it belongs too
    def find(self,x):
        if self.parents[x] == x:
            return x 
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]
        
    # if parents are different, joins them and decrements number of friend groups
    def union(self,a,b):
        #find parents
        group1 = self.find(a)
        group2 = self.find(b)
        #join them
        if group1 != group2:
            self.parents[group1] = group2
            self.count-=1

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        #if empty, return 0 
        if len(M) == 0:
            return 0
        #union find class instance
        uf = UnionFind(len(M))
        
        #iterate through matrix
        for i in range(len(M)):
            for j in range(len(M[0])):
                #if relationship between two people, perform union
                if M[i][j] == 1 and i != j:
                    uf.union(i,j)
        return uf.count