import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        #if string empty
        if len(s) == 0:
            return -1
        
        index_table = dict()
        count_table = dict()
        visited = []
        
        for index in range(len(s)):
            #if we haven't seen this char before 
            if s[index] not in index_table:
                #log the index of first appearance
                index_table[s[index]] = index
                #start count for char 
                if s[index] not in count_table:
                    count_table[s[index]] = 1
                #place char in visited array 
                if s[index] not in visited:
                    visited.append(s[index])
        
            #update count 
            else:
                count_table[s[index]] += 1
        #go down order of visited characters
        for char in visited:
            #return first instance of non repeated character
            if count_table[char] == 1:
                return index_table[char]
                
        #return -1 if no such character found
        return -1