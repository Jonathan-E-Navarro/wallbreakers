class Solution:
    '''
    each entry in dp is the max profit that can be attained by robbing all allowable 
    houses up to this one
    table entry [0] = robbing the first house 
    table entry [1] is the max (profit deciding to rob the first house vs deciding this one instead) 
    table entry [i] is max(profits from robbing houses up the one behind this one  vs profits from robbing houses up the     2 behind this one and including this one)
    '''
    def rob_houses(self, nums: List[int]) -> int:
        n = len(nums)
        if not nums: 
            return 0
        if len(nums)==1: 
            return nums[0]
        memo = [0]*n
        memo[0],memo[1] = nums[0],max(nums[1],nums[0])
        for i in range(2,n):
            # print(dp)
            memo[i]=max(memo[i-1],memo[i-2]+nums[i])
        # print(dp)
        # print("\n")
        return memo[-1]
    
    
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        h1 = nums[:-1]
        h2 = nums[1:]

        r1 = self.rob_houses(h1)
        r2 = self.rob_houses(h2)
        return max (r1,r2)
    
        