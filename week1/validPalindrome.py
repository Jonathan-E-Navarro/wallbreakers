class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l1 = []
        for char in s:
            if char.isalnum():
                l1.append(char.lower())
        l2 = l1[:]
        l1.reverse()
        if l1 == l2:
            return True
        return False

"""
Thought process:
first we have to make sure we are only considering alphanumeric characters and ignore cases. 

so what we can do is iterate through the string and check whether the character 
is alphanumeric, if so, we lower it and add it to a list 

then we can make a reversed copy of that same list of characters 

if they are equal to eachother, then they are palindromes (same characters in same order)
"""