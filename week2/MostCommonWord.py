from collections import Counter
import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub('[\W_]', ' ', paragraph.lower()).split()
        banned_set = set(banned)
        count = Counter()
        
        for word in paragraph:
            if word not in banned_set:
                count[word]+=1
                
        max_value = max(count.values())
        for key,value in count.items():
            if value == max_value:
                return key
        