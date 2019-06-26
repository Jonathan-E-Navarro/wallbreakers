#This uses a hashmap to speed up lookup time 
#Uses one pass 
'''
instead of doing: iterating to put all nums in map 
and iterating again to check if complement exists in 

We do: while iterating to put nums in hashmap, we check if the complement exists in the same loop
'''
class Solution(object):
    def twoSum(self, nums, target):
        hashmap = dict()
        for i in range(len(nums)):
            complement = target-nums[i]
            #if complement in map and not nums[i]
            if complement in hashmap and hashmap[complement]!=i:
                return [i,hashmap[complement]]
            #store the index mapped to the value for quick lookup
            hashmap[nums[i]]=i

