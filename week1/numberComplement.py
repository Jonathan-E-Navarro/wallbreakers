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

"""
Thought process:
python syntax tests:
print(num)
limit = (231) - 1
print(num ^ limit)
print(abs(~num))
print(bin(num))
for x in str(bin(num))[2:]:
			print("num",x)
			print("flipped: ",int(x)^1)**
		
There are two ways to do this :
1. converting the number to binary and xoring with proper amount of 1's  
we can  create the proper size  mask  by creating the largest 32 bit binary 
number and then reducing its size to the length of our binary number to be compared
2. iterating through and xoring with 1's
			
"""
    
    
            
    
        
        