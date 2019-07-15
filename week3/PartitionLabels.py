from collections import Counter
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        results = []
        finished = Counter(S)
        counts = Counter()

        idx = 0 
        while idx < len(S):
            counts[S[idx]]+=1
            
            accepted = True
            for count in counts:
                if counts[count]!=finished[count]:
                    accepted = False
                    break
                    
            if accepted:
                _sum = sum([counts[x] for x in counts])
                results.append(_sum)
                counts.clear()
            idx+=1
                
        return results
                