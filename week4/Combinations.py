class Solution:
    def __init__(self):
        self.ans = []
        self.current = []
        self.k = None
        self.n = None
    def backtrack(self,idx):
        #if rabbit hole end,
        if len(self.current) == self.k:
            #add current combo to our answer list 
            # print("rabbit hold ended with: ",self.current)
            self.ans.append(self.current[:])
        else:
            for i in range(idx, self.n+1):
                # print("idx level: ",idx)
                #add num to current combo
                self.current.append(i)
                # print("current: ",self.current)
                #go down the rabbit hole  
                self.backtrack(i+1)
                #pop last num off to advance to the next num in combination for this spot in the array
                self.current.pop()
                
        
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.k = k
        self.n = n 
        #start at index 1 since range zero indexs, we will add 1 to n later
        self.backtrack(1)
        return self.ans