class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        new_matrix = [[None] * len(A) for num in range(len(A[0]))]
        for row in range(len(A)):
            for col in range(len(A[0])):
                new_matrix[col][row] = A[row][col]
        return new_matrix
      
        
            