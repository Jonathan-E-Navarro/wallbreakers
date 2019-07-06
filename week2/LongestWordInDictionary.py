from collections import Counter 
class Solution:
    def longestWord(self, words: List[str]) -> str:        
        word_set = set(words)
        # buildable = Counter()
        max_len = 0 
        candidates = []
        
        #search all words
        for word in word_set:
            applicable = True
            test = word[:]
            while len(test) > 0:
                if test in word_set:
                    test = test[:-1]
                else:
                    applicable = False
                    break
                    
            #if word can be built one at a time by other words in word set
            if applicable:
                #add to candidates list
                candidates.append(word)
                #record current max length
                if len(word)>max_len:
                    max_len = len(word)
                    
                    
#                 #make lexicographic scores for words and put it in a counter
#                 for char in word:
#                     buildable[word]+=ord(char.lower())-ord("a")+1
    
        #filter candidates by max length 
        candidates = [candidate for candidate in candidates if len(candidate) == max_len]
        #min compares strings lexicographically 
        return min(candidates)
    
        #This was when I using a lexicographic counter dictionary 
        #then I found out that min compares strings lexicographically so I dont need it 
        # len_candidates =[(x,buildable[x]) for x in buildable if len(x) == max_len]
        # return min(len_candidates)[0]
        
        
        
                
               
        