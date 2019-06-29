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

"""
Thought process:
Thought process notes:
if A and B are friends,
and B is friends with C, we have one friend group 

if A and B are friends, 
and C and D are friends, we have 2 groups 

if A and B are friends, 
and C has no friends, we have2 groups 

if M[i,j] =1, then M[j,i] =1 

[[1,1,0],
 [1,1,0],
 [0,0,1]]
 
 M[0][0] and M[0][0] means 0 friends with himself
 M[0][1] and M[1][0] means 0 and 1 are friends
 M[0][2] and M[2][0] means 0 and 2 not friends
 M[1][1] and M[1][1] means 1 friends with himself
 M[1][2] and M[2][1] means 2 and 1 not friends
 M[2][2] and M[2][2] means 2 is friends with himself 
 
 group 1 : 0 and 1.  group 2: 2 
 how to achieve this? 
 make sets, check for membership, if not member, start group 
 if member, pass 
 
 simulation iteration:
  M[0][0] and add M[0][0] to seen, no set with 0, create and add to set (0)
	M[0][1] and add M[1][0] to seen, set with 0 in it, so add 1 into that set (0,1)
	M[0][2] and add M[2][0] to seen, 0 so ignore
	M[1][1] and add M[1][1] to seen, set with 1 in it already so ignore
	M[1][2] and add M[2][1] to seen, 0 so ignore 
	M[2][2] and add M[2][2] to seen, no set with 2 in it, so create and add (0,1)(2)
	count number of sets: 2 
	
	
[[1,1,0],
 [1,1,1],
 [0,1,1]]
 
 M[0][0] and M[0][0] means 0 friends with himself
 M[0][1] and M[1][0] means 0 and 1 are friends
 M[0][2] and M[2][0] means 0 and 2 not friends
 M[1][1] and M[1][1] means 1 friends with himself
 M[1][2] and M[2][1] means 2 and 1 are friends
 M[2][2] and M[2][2] means 2 is friends with himself 
 
 [[1,1,0],
 [1,1,1],
 [0,1,1]]
 simulation iteration:
  M[0][0] and add M[0][0] to seen, no set with 0, create and add to set (0)
	M[0][1] and add M[1][0] to seen, set with 0 in it, so add 1 into that set (0,1)
	M[0][2] and add M[2][0] to seen, 0 so ignore
	M[1][1] and add M[1][1] to seen, set with 1 in it already so ignore (or add redundant)
	M[1][2] and add M[2][1] to seen, set with 1 in it, so add 2 into that set (0,1,2)
	M[2][2] and add M[2][2] to seen, set with 2 in it so ignore or add redundant (0,1,2)
	count number of sets: 1
	
	This approach didn't account for instances like 
	(0,1,2) (3,2), could not perform union
	
	This is where the union find approach comes in!
	
"""