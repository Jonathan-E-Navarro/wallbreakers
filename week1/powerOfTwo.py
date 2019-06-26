import math 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n!= 1:
            if n%2 != 0 or n == 0:
                return False
            n = n/2
        return True
                    
        