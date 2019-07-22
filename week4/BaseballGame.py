class Solution:
    def calPoints(self, ops: List[str]) -> int:
        result = 0 
        rounds = []
        for i in range(len(ops)):
            if ops[i].strip('-').isdigit():
                result+=int(ops[i])
                rounds.append(int(ops[i]))
            
            elif ops[i] == "+":
                result+= (rounds[-1]+rounds[-2])
                rounds.append(rounds[-1]+rounds[-2])
                
            elif ops[i] == "C":
                result-= rounds[-1]
                rounds.pop()
                
            elif ops[i] == "D":
                result+= (2*rounds[-1])
                rounds.append(2*rounds[-1])
                        
        return result
        