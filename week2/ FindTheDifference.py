from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for key,count in (t_count-s_count).items():
            return key
            
      