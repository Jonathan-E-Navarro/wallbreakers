class Solution:
    def reverseWords(self, s: str) -> str:
        
        # first method 
        s2 = s.split()
        for word in range(len(s2)):
            s2[word] = s2[word][::-1]
        return " ".join(s2)
    
        # #second method 
        # s = s[::-1]
        # sp = s.split()
        # sp = sp[::-1]
        # # print(sp)
        # sp = " ".join(sp)
        # return sp

