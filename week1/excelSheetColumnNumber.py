class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0 
        for digit in s:
            result = result*26 + (ord(digit)-ord('A')+1) 
        return result
        