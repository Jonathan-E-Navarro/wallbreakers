import math 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n!= 1:
            if n%2 != 0 or n == 0:
                return False
            n = n/2
        return True
                    
"""
Thought process:
1 is a power of 2 because 2^0 = 1 and 0 is not a power of 2 because there is no 
number we can power 2 by to get 0 

Other than those facts, we can tell that a number is a power of 2 if it is 
divisble by 2, in other words, if that number/2 produces no remainder 

we can do something simple like:
 
 if n == 1: True 
 if n%2 != 0 or n==0: return False
"""       