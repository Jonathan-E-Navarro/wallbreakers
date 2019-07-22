class Solution:
    def isValid(self, s: str) -> bool:
        """
        :type s: str
        :rtype: bool
        """
        #stack for last seen opening bracket 
        prev = []
        types = {")":"(","}":"{","]":"["}

        for bracket in s:
            #if we have a closing bracket
            if bracket in types:
                #if stack non empty, 
                if prev:
                    top = prev.pop()
                else:
                    #if stack is empty, then that means we have
                    #received a closing bracket and no previous open bracket
                    #so we just return False since thats invalid
                    return False
                
                #if the open bracket mapped to current closing bracket
                #does not match the current previous open bracket, false 
                if types[bracket]!=top:
                    return False
            else:
                #we have a opening bracket, push onto stack of previous
                #open brackets 
                prev.append(bracket)
                
    
        #if stack is empty by this point,then our parenthesis have been valid 
        if not prev:
            return True
        return False
            
                
                
        
                