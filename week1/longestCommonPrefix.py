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
        
        