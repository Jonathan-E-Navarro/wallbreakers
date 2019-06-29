class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #if carry not going to happen, just add 1 to least significant digit 
        if digits[-1] != 9:
            digits[-1]+=1
        
        else:
            #first carry is going to be one because of 9 about to become 0 
            carry = 1
            for i in reversed(range(len(digits))):
                #set prev to digit before modification
                prev = digits[i]
                #digit = digit+carry%mod10  (this causes 9+1 to revert back to 0)
                digits[i] = (digits[i]+carry)%10
                
                #if new digit == 0 and previous digit!= 0  accounts for instances like 
                #101 -> 102 when we hit 0+carry(0), and get 0, since it did not change from 9->0 we do not carry 1 
                if digits[i] == 0 and digits[i] != prev:
                    carry = 1
                else:
                    carry = 0
                
            #digit overflow handling 
            if digits[0] == 0:
                digits.insert(0,1)
        
        return digits

"""
Thought process:

Maybe we can think about doing this just as we would by hand,
we iterate from the right to left, add 1 to the least significant digit 
and then move to the left handling carry digits if necessary. 

Soooo, we itereate through list from left to right, and add 1 to LSD before 
iteration begins, and then handle carry digits throughout iteration. 

We can use mod10 to handle returning 9 -> 0 since 10mod10 = 0
"""