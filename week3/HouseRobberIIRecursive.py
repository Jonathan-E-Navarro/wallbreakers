class Solution:
    '''
    each entry in dp is the max profit that can be attained by robbing all allowable 
    houses up to this one
    table entry [0] = robbing the first house 
    table entry [1] is the max (profit deciding to rob the first house vs deciding this one instead) 
    table entry [i] is max(profits from robbing houses up the one behind this one  vs profits from robbing houses up the     2 behind this one and including this one)
    '''
    def __init__(self):
        self.memo = dict()

    def rob_houses_recursive(self,i,nums):
        if i >= len(nums):
            return
        
        self.memo[i]=max(self.memo[i-1],self.memo[i-2]+nums[i])
        self.rob_houses_recursive(i+1,nums)
        
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        h1 = nums[:-1]
        h2 = nums[1:]
        
        if not h1: 
            result1 = 0 
        elif len(h1)==1: 
            result1 = h1[0]
        
        else:
            self.memo[0],self.memo[1] = h1[0],max(h1[1],h1[0])
            self.rob_houses_recursive(2,h1)
            result1 = self.memo[len(h1)-1]
                    
        self.memo.clear()
        
        if not h2: 
            result2 = 0
        elif len(h2)==1: 
            result2 = h2[0]
        else:
            self.memo[0],self.memo[1] = h2[0],max(h2[1],h2[0])
            self.rob_houses_recursive(2,h2)
            result2 = self.memo[len(h2)-1]
        
        return max(result1,result2)