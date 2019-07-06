class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0 
        jewels = dict()
        for jewel in J:
            if jewel not in jewels:
                jewels[jewel] = 1
                
        for stone in S:
            if stone in jewels:
                count+=1
        return count
                
        