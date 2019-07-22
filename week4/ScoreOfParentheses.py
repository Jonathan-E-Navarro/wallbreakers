class Solution(object):
    def scoreOfParentheses(self, S):
        stack = []
        stack.append(0)
        score = 0
        ans = 0
                    
        for i in range(len(S)):
            if S[i] == '(':
                score = score*2 if score != 0 else 1
        
            elif S[i] == ')':
                if S[i-1] == '(':
                    ans+= score
                score = score//2 
                    
        return ans         
    