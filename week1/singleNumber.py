class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            table[num]=table[num]+1 if num in table else 1
            
        for num,count in table.items():
            if count == 1:
                return num 

"""
Thought process:
what we're basically gonna do in this problem is count instances of 
various things, and return the one with the least amount of instances, in this case 1. 

For creating multiple counts with neat quick lookup, nice membership 
testing features, I like to use a hashmap or in python's case, a dictionary.

we iterate through the nums and add the amount of instances to their 
corresponding spots in the hashtable.

then we go through the hashtable and return the num whose instance == 1
"""