class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        new_matrix = [[None] * len(A) for num in range(len(A[0]))]
        for row in range(len(A)):
            for col in range(len(A[0])):
                new_matrix[col][row] = A[row][col]
        return new_matrix
      
        
"""
Thought process:
In linear algebra, the transpose of a matrix is an operator which flips a matrix over its diagonal, 
**that is it switches the row and column indices of the matrix** by producing another matrix denoted 
as 
AT (also written A′, Atr, tA or At).

we have an M X N matrix
so what we can do is create a new empty matrix with the following dimensions N X M

We iterate through our M X N matrix and new_matrix [col][row] = old_matrix[row][col]

and we return the new matrix :]



"""