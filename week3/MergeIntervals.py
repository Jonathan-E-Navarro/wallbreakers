class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        if len(intervals) == 0:
            return []
        result = []
        current = 0
            
        for interval in intervals:            
            if not current:
                current = interval
            else:
                if interval[0] in range(current[0],current[1]+1):
                    current[1] = max(current[1],interval[1])
                else:
                    result.append(current)
                    current = interval 
        result.append(current)
        return result