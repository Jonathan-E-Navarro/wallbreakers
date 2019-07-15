class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = [char for char in s]
        t = [char for char in t]
        s.sort()
        t.sort()
        if s == t:
            return True
        return False
    