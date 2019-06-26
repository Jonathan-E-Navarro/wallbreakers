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