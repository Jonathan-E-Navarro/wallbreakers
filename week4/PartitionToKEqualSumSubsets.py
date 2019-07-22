
class Solution:
    def __init__(self):
        self.nums = None
        self.partitions = None
        
    def search(self,i):
        #if we've exhausted all of our nums, then its true
        if not self.nums:
            return True
        #we pop an element off nums to add to our subset
        v = self.nums.pop()
        for j, part in enumerate(self.partitions):
            if part + v <= self.target:
                self.partitions[j]+=v
                if self.search(i+1):
                    return True
                self.partitions[j]-=v
            if not part:
                break
        self.nums.append(v)
        return False

    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        #each of our subsets need to equal to our target value
        self.target = sum(nums)/k
        #our remainder when trying to get our subset goal
        rem = sum(nums)%k
        #if our remainder isnt zero, then we cant evenly divide, so false
        #or if our max num is greater than our subset goal
        if rem!=0 or max(nums) > self.target: return False

        #sort our nums to speed up our search 
        nums.sort()
        self.nums = nums
        #list of partitions 
        # partitions = [0]*k
        self.partitions = [0]*k
        return self.search(0)
        
        