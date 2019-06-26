class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:    
        for i in range(len(A)):
            A[i] = A[i][::-1]
            
        for row in range(len(A)):
            for col in range(len(A[0])):
                A[row][col] = A[row][col] ^ 1
                
        return A

        