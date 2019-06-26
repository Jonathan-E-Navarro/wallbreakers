class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        table1 = dict()
        table2 = dict()
        
        for char in s:
            table1[char] = table1[char]+1 if char in table1 else 1
        for char in t:
            table2[char] = table2[char]+1 if char in table2 else 1
            
        if table1 == table2:
            return True
        else:
            return False
            
        