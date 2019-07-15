from bisect import bisect, bisect_left
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        results=[]
        p_list = sorted(p)
        prev_idx = 0 
        window = sorted(s[:len(p)])
        
        for i in range(len(p),len(s)+1):            
            if window == p_list:
                results.append(i-len(p))

            prev = s[prev_idx]
            window.remove(prev)
            
            if i<len(s):
                window.insert(bisect(window,s[i]),s[i])
                
            prev_idx+=1
        
        return results

            