class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums = sorted(nums)    
        # nums.sort()
        result = 0 
        idx = 1
        while idx < len(nums):
            result+=min(nums[idx-1],nums[idx])
            idx+=2
        return result
        
        