from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        p1 = 0 
        p2 = len(p)
        
        results = []
        #counter for p 
        p_count = Counter(p)
        
        #counter window for s 
        checker = Counter(s[p1:p2])
        while p2<=len(s):
            # print(checker)
            # print(s[p1:p2])
            
            #check for anagram
            if checker == p_count:
                results.append(p1)
            #remove first character in window
            checker[s[p1]]-=1
            if checker[s[p1]] == 0 :
                del checker[s[p1]]
            
            #add character outside window
            if p2+1 <= len(s):
                # print("p2: ",s[p2])
                checker[s[p2]]+=1
            
            p1+=1
            p2+=1
        
        # print(checker)
        if checker == p_count:
                results.append(p1)
        return results
        