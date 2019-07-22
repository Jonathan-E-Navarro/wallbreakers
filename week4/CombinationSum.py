class Solution:
    def __init__(self):
        self.combo = []
        self.combos =[]
    def explore(self,candidates,start,target):
        # print(self.combo,target,self.combos)
        if target == 0:
            #we have found a valid solution
            # combos.append(combo)
            self.combos.append(self.combo[:])
            return 
        elif target < 0:
            #we lose hope and backtrack
            return
        
        for i in range(start,len(candidates)):
            #add new candidate to current combo
            self.combo.append(candidates[i])          
            self.explore(candidates,i,target-candidates[i])
            #if and when back track happens, the original with out the 
            #added candidate will be used
            self.combo.pop()
            
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.explore(candidates,0,target)
        # print(self.combos)
        return self.combos
        