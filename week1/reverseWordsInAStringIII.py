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

"""
Thought process:
We need to reverse the words while maintining the original order,

we can split the string into words, iterate through list of words 
and reverse them using [::-1] and then join the string 

or we can reverse the string first using [::-1], split the words 
into a list, reverse the list order and then join 
"""