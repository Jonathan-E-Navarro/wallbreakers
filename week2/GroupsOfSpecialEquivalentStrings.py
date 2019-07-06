class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        '''
        two strings are special equivalent if they can become each other 
        by swapping only even chars with even chars and odds with odds 
        
        how can we count these groups? 
        
        we can sort the string and add that to a set. 
        if one group/set of unique chars can be shifted to create numerous combinations, thenn
        keeping track of unique sets of characters = one group that can be shifted around numerous times
        and the number of these unique sets of characers  = number of groups
        
        we do this by creating a list like [all odds followed by evens] 
        so even different strings return the same list because they have the same odd even placement
        '''
        length = len(A)
        results = set()
        for item in A:
            odds = item[::2]
            evens = item[1::2]
            results.add( str(sorted(odds) + sorted(evens))) 
            # print(str(sorted(odds) + sorted(evens)))
            # print(results)
        return len(results)
        