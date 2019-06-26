class Solution:
    #hamming distance is calculated by xoring both numbers 
    #and counting the amount of 1's (spaces that differed)
    def hammingDistance(self, x: int, y: int) -> int:
        return len(bin(x^y)[2:].replace('0',''))
        