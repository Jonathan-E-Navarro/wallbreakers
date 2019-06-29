class Solution:
    #hamming distance is calculated by xoring both numbers 
    #and counting the amount of 1's (spaces that differed)
    def hammingDistance(self, x: int, y: int) -> int:
        return len(bin(x^y)[2:].replace('0',''))

"""
Thought process:
Hamming distance is the number of bit positions that are different amongst two binary numbers. 

A cool way to do this is to xor the numbers together. xor produces 1 if and 
only if the two bits in question are different, so we can count the number of 1's 
that this xor operation produces and that will be our hamming distance
			
"""