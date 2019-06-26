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