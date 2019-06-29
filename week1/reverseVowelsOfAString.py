class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u']
        p1 = 0  
        p2 = len(s)-1
        swap1 = 0
        swap2 = 0 
        
        s = [char for char in s]

        while p2 > p1:
            if s[p1].lower() in vowels:
                swap1 = 1
            if s[p2].lower() in vowels:
                swap2 = 1
                
            if swap1 == 1 and swap2 == 1:
                s[p1],s[p2] = s[p2],s[p1]
                swap1 = 0
                swap2 = 0 
            p1 = p1+1 if swap1 == 0 else p1
            p2 = p2-1 if swap2 == 0 else p2
        s = "".join(s)
        return s

"""
Thought process:
we want to reverse only the vowels of a string, what does this mean?

From what I've seen with their examples, it appears that a reverse vowel mean this 
if there is a vowel at s[0] and one at s[len-1], swap em and keep closing in from both sides

This is screams two pointers to me 
initalize one pointer at 0 and the other at len(str)-1
so while the pointers have not crossed each other,
if both pointers are currently pointing to a vowel, swap em 
"""