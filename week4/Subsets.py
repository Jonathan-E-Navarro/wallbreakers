class Solution:
    '''
                                        []
                           []                       [1]
                    [2]           []          [1,2]      [1]
                 [2]  [2,3]    [3]  []
    
    trick to the method
    take cs dojos tree explanation and turn it into an iterative O(n) algorithm 
    []
    []   add [item+[num] for item in res] => [1] and join with answer
    [][1]  add [item+[num] for item in res] => [2][1,2]  and join with answer 
    [][1][2][1,2]  add [item+[num] for item in res] => [1,3][2,3][1,2,3] and join with answer
    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:            
        ans = []
        ans.append([])  #add empty set 
        for num in nums:
            sublist=[]
            for element in ans:
                sublist.append(element+[num])
            ans += sublist
            
                
        return ans
        
    
        
    
            
        
        