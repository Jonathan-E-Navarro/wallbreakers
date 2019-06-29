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
            
"""
Thought process:
For creating multiple counts with neat quick lookup, nice membership 
testing features, I like to use a hashmap or in python's case, a dictionary.

we iterate through both strings and add their char counts to their 
respective dictionaries and then compare the two.
"""