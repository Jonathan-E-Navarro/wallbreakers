class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        d = dict()
        for idx in range(len(s)):    
            #if s char not in dictionary
            if s[idx] not in d:
                #check for double mapped t chars
                if t[idx] in d.values():
                    return False
                #t char not mapped to anything else, map this t char to this s char
                d[s[idx]] = t[idx]
            #if s char in dictionary and its t char does not match this t char, return false
            elif s[idx] in d and d[s[idx]]!=t[idx]:
                return False
        return True
        