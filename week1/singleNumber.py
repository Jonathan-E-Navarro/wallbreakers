class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = dict()
        for num in nums:
            table[num]=table[num]+1 if num in table else 1
            
        for num,count in table.items():
            if count == 1:
                return num 
        