class Solution:
    def binaryGap(self, N: int) -> int:
        max_gap = 0 
        N = bin(N)[2:]
        seen = False
        count = 0
        for digit in N:
            if digit == '1' and not seen:
                seen = True
            elif digit == '1' and seen: 
                count+=1
                max_gap = max(max_gap,count)
                count = 0 
            else:
                count+=1  
        return max_gap
            
        