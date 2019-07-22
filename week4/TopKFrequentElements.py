from collections import Counter 
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter()
        ans = []
        for num in nums:
            # print(num)
            counts[num]+=1

        # print(counts)
        # frequents = [(key, counts[key]) for key in sorted(counts, key=counts.get, reverse=True)]
        frequents = [key for key in sorted(counts, key=counts.get, reverse=True)]
        # print(frequents[:k])
        return frequents[:k]
        
        