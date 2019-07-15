class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort()
        g.sort()
        count = 0
        for child in g:
            content = False
            idx = 0 
            while not content and idx<len(s):
                if s[idx]>= child:
                    s.remove(s[idx])
                    count+=1
                    break
                idx+=1
        return count
            
        