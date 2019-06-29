class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:    
        for i in range(len(A)):
            A[i] = A[i][::-1]
            
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] = A[row][col] ^ 1
                
        return A

"""
Thought process:
We want to flip the image horizontally and invert the bits: so we can do this 

To flip image horizontally: 
We iterate through rows of the matrix and do row = row [::-1]
This effectivley goes through the matrix and sets each row to a
 horizontally flipped version of itself

To invert the bits:
All we have to do is iterate through the matrix and set each bit to the 
result of xoring said bit with 1 to flip it
"""