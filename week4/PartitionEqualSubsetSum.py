class Solution:  
    def canPartition(self, nums: List[int]) -> bool:
        #first check if we can even get an even division in half
        total = sum(nums)
        if total % 2 == 1:
            return False
        
        #our goal is to find half of the equal subset
        #if one half exists then the other must as well  
        #since at this point we have verified that a clean split is possible 
        target = total // 2
        #reverse sort the list so that its easier/faster to find a subset or num 
        #that equals the half point
        nums.sort(reverse=True)
        #explore possible subsets
        #for reach num 
        for i in range(len(nums)):
            _sum = 0
            #for each other num, build a sum 
            for j in range(i, len(nums)):
                if _sum + nums[j] == target:
                    return True
                elif _sum + nums[j] < target:
                    _sum += nums[j]
        return False
       