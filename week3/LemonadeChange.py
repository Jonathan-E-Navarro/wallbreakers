from collections import Counter 
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = Counter()
        for bill in bills:
            if bill == 5:
                #just add it to the register 
                register[bill]+=1
            elif bill == 10:
                #we must return 5 dollars 
                if register[5] != 0:
                    register[5]-=1
                    register[bill]+=1
                else:
                    return False
            elif bill == 20:
                #we must return 15 dollars one 10 and a 5 or three 5's 
                if register[10]!=0 and register[5]!=0:
                    register[10]-=1
                    register[5]-=1
                    register[bill]+=1
                elif register[5] >= 3:
                    register[5]-=3
                    register[bill]==1
                else:
                    return False
        return True
                        