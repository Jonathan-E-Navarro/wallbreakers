from collections import Counter
class Solution:
    def countOfAtoms(self, formula: str) -> str:
        reverse = formula[::-1]
        tracked = ''
        element = ""
        multipliers = [1]
        counts = Counter()
        
        for char in reverse:
            if char.isdigit():
                tracked= char + tracked
    
            elif char == ")":
                multipliers.append(int(tracked)*int(multipliers[-1]))
                tracked = '' 
                
            elif char == "(":
                multipliers.pop()
                
            elif char.isalpha() and char.islower():
                element = char+element
                
            elif char.isalpha() and char.isupper():
                element =char+element
                if tracked != '':
                    counts[element] += int(tracked)*int(multipliers[-1])
                else:
                    counts[element] +=1*int(multipliers[-1])
                element = '' 
                tracked = ''
                
        l1 = []
        for key in sorted(counts.keys()):
            if counts[key] > 1:
                l1.append(key+str(counts[key])) 
            else:
                l1.append(key)
        return "".join(l1)

                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
  