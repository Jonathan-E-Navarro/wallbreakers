class Solution:
    '''
    3 keys:
    1. our choice : place ( or )
    2. constraints: cannot close a bracket until there is an open bracket
       so we need to take the amount of open brackets into account 
    3. goal: we want 2*n total brackets
    
    we can use opening brackets as long as the amount of opening brackets is less than closing brackets
    
    sample logic run through observation: when back tracking we backtrack to the previous string that still had 
    opening brackets available and add a ) to go down and come up with a new combo 
    
    n= 3 
    ( we can still use more opens 
    (( we can still use more opens 
    ((( no more opens can be used, add closing 
    ((() closing still < open add closing
    ((()) closing still < open add closing
    ((())) we have reached a valid combo append it and back track 
    
    (( this our string after we back track go to next case and add ) 
    (() we can still use more opens 
    (()( no more opens can be used add closing
    (()() no more opens can be used add closing 
    (()()) valid combo reached, add it to array and back track 
    
    (() this our string after we back track go to next case and add ) 
    (()) we can still use more opens 
    (())( no more opens can be used 
    (())() valid combo 
    '''
    def __init__(self):
        self.n = None
        self.ans = []
    def backtrack(self,string,opening,closing):
        #if len == number of brackets in a combo, we have a combo so append combo 
        # print(string)
        if len(string) == 2 * self.n:
            self.ans.append(string)
            return

        #if amount of open brackets < N, we still can use open brackets, 
        if opening < self.n:
            self.backtrack(string+'(', opening+1, closing)
            #here we exit the above back track and execute the next if 
            # print("open brackets: ",string)

        #if amount of closing brackets < open brackets, we can still closing brackets 
        if closing < opening:
            self.backtrack(string+')', opening, closing+1)
            #by this point we have added another valid parenthesis combo 
            # print("backtracking")

        # print(string)
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n 
        self.backtrack('',0,0)
        return self.ans

