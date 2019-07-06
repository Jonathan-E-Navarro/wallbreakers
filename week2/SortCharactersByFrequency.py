from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        result = ""
        counts = Counter(s)
        
        #create a list of key,value tuples in descending order of amount seen
        sorted_pairs = [(k, counts[k]) for k in sorted(counts, key=counts.get, reverse=True)]
        
        #for pair in list, add char the number times it appears to our result
        for pair in sorted_pairs:
            result+=(pair[0]*pair[1])
            
        #return result string
        return result

        