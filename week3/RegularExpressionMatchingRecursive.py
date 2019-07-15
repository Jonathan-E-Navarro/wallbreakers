'''iterative recursive version'''
class Solution(object):
    def match(self,s,i,p,j):
        if i == -1 or j == -1:
            return False 
        return p[j] == '.' or s[i] == p[j]   

 

    def case_checker(self,s,i,p,j):
        # print("i: ",i,"j: ",j)
        # Base Cases
        #if no more pattern 
        if j == -1:
            #if no more string as well, we return true else false 
            return i == -1 
        # to cover the case of "abc" ".*", in case we running on off our string 
        if i < -1:
            return False
        
        
        # 1. if  p[j] is * check on p[j-1]
        if p[j] == '*' and j >= 1:
            #      check if match with char  check for repeats with same pattern    check without that char*
            return (self.match(s, i, p, j-1) and self.case_checker(s, i-1, p, j)) or self.case_checker(s, i, p, j-2)
            
        # 2. Match either same or '.'
        if self.match(s, i, p, j):
            #move down for both 
            return self.case_checker(s, i-1, p, j-1)
        # 3. No match or *
        return False 

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        return self.case_checker(s,len(s)-1,p,len(p)-1)