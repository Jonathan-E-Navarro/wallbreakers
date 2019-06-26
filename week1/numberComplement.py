class Solution:
    def findComplement(self, num: int) -> int:
    # converting number to binary and xoring with proper amount of 1's        
        num = bin(num)[2:]
        limit = bin((2**31) - 1)[2:len(num)+2]

        # print(num,limit)
        complement = abs(int(num,2)) ^ abs(int(limit,2))
        return(complement)

# # iterating through and xoring with 1's 
#         l1 = []
#         for x in str(bin(num))[2:]:
#             l1.append(str(int(x)^1))
        
#         flipped = "".join(l1)
#         return(int(flipped,2))

# list comprehension: you happy Pattis?
        # return int("".join(str(int(x)^1) for x in bin(num)[2:]),2)

    
    
            
    
        
        