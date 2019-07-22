class Solution:
    '''
    00 xor 00 => 00
    01 xor 00 => 01
    10 xor 01 => 11 
    11 xor 01 => 10 
    
    10101 xor 01010 = > 11111
    10110 xor 01011 =>  11101
    
    if you take a number and xor it with it shifter to the right once,
    the answer will differ by one digit from the previous numbers answer 
    
    
    '''
    def grayCode(self, n: int) -> List[int]:
        ans = []
        for i in range(1 << n):
            ans.append(i ^ (i >> 1))
        return ans
        