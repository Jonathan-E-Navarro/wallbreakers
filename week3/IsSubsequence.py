class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
         
        built = ''
        idx = 0 
        
        for char in t:
            if idx < len(s):
                if char == s[idx]:
                    built+=s[idx]
                    idx+=1
                    
        if built == s:
            return True
        
        return False
        