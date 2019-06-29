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

"""
Thought process:
logic tests:
1000
0123
101
012

111
01
		01
			 0
1100100
01
		0123
						 01   
						 
when 1 and not seen,  set seen
when 0, count+=1 
when 1 and seen,  count+=1, calculate new max_gap 


"""
