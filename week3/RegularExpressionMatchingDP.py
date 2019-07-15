class Solution(object):
    '''
    table is an array that represents the entries in a 2D table.
    table[(i,j)] represents whether the entry in the table for char i in 
    s and char j in p is either True or False
    '''
    def isMatch(self, s, p):
        table = dict()
        #initalize entry 0,0 to be True in the case of empty strings 
        table[(0,0)] = True
        
        #initalized every entry in the 0 column to be false 
        #in the case that s is non-empty and p is empty 
        for i in range(len(s)):
            table[(i+1,0)] = False

        #initalize every entry in the 0 row 
        #False if it is a char or .
        #if it is a *, then look back two before the char before and set 
        #the entry to where that char was true or false 
        #useful for cases like s: ""  p: "a*b*"
        for j in range(len(p)):
            if p[j] =="*":
                table[(0,j+1)] = table[(0,j-1)]
            else:
                table[(0,j+1)] = False

        #loop through and fill in table 
        for i in range(len(s)): 
            for j in range(len(p)):
                #if same or ., True 
                if s[i] == p[j] or p[j]==".":
                    table[(i+1,j+1)] = table[(i,j)]
                #if *, look two behind and set it to that
                elif p[j] == "*":
                    table[(i+1,j+1)] = table[i+1,j-1]
                    if not table[i+1,j+1]:
                        if p[j-1] == s[i] or p[j-1] == ".":
                            table[(i+1,j+1)] = table[(i,j+1)]
                            
                #else this entry is false
                else:
                    table[(i+1,j+1)] = False
                     
        #return last entry in table
        return table[len(s),len(p)]
        
        
        
  