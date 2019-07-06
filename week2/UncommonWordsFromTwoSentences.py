class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        table = dict()
        results = []
        for word in A.split():
            if word not in table:
                table[word] = 1
            else:
                table[word]+=1
        for word in B.split():
            if word not in table:
                table[word] = 1
            else:
                table[word]+=1
        
        for word,count in table.items():
            if count == 1:
                results.append(word)
                
        return results

