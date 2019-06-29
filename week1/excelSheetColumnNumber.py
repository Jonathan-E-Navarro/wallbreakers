class Solution:
    def titleToNumber(self, s: str) -> int:
        result = 0 
        for digit in s:
            result = result*26 + (ord(digit)-ord('A')+1) 
        return result

"""
Thought process:
Ok 

A = > 1     so we use ord(char)-ord(A) to find value 

AB = >   28   so we use ord(A)-ord(A) to get 1 but we 
need to edit this later to 26 if there's more later
so we use ord(B)-ord(B) to get 2  and we edit our last result to result*26

This ensure we get a consistent answer 
if we have for example four A's  the way this is calculated is :

result = first A = 1 
result = result*26 (to account for the first A's new value since we've done one
passthrough)+A (1) => 27 for AA
result = result*26(to account for second passthrough) + A(1) =>702+1 =703
"""