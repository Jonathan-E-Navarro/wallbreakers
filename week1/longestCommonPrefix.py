class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0 :
            return ""
        #initalize prefix as first string
        prefix = strs[0]
        #scan and compare to rest of strings    
        # for each word 
        for i in range(1,len(strs)):
            #While prefix still not substring of word
            searching = True
            while searching:
                try:
                    index = strs[i].index(prefix) 
                except:
                    index = -1
                    
                if index != 0:
                        #decrement prefix
                        prefix = prefix[0:len(prefix)-1]
                        #if empty string, no common prefix
                        if len(prefix) == 0:
                            return ""
                else:
                    # print(index)
                    searching = False
                    
        return prefix
        
        
"""
Thought process:
we need a way to count and or track prefixes 

well we know that a prefix is going to be a subset of the word that starts at the 
beginning, and if its a common prefix, then it should be present in every word

so if there is a common prefix, it should be in any word we choose, so we can 
arbitrarily set our inital LCP as the entire first string. the reason why is this:

we iterate through our strings starting from the second and compare it to our prefix,
while our prefix is not a subset of our word and does not start at index 0:
we chop a character off until it is a prefix or until we get 0 chars in which 
the case is that a common prefix does not exist 

we do this comparison and operation for every string after the first. 
"""