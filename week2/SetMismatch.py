from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        counts = Counter(nums)
        range_set =set([num for num in range(1,len(nums)+1)])
        results = []
        
        #find num that repeats and add it to result list
        for key,count in counts.items():
            if count == 2:
                results.append(key)
        
        #find difference between our correct range set and our nums set
        #the differnce will be the num that was incorrectly ommitted from nums 
        #add that to our results list
        results.append(range_set.difference(set(nums)).pop())
        return results
                
                