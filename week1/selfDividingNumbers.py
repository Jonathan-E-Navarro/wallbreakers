class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []
        valid = 0 
        #iterate through range of numbers
        for num in range(left,right+1):
            #for digit in num 
            for digit in str(num):
                #if digit is 0 or num/digit has remainder, 
                if int(digit) == 0 or num%int(digit)!=0:
                    #not valid, break out of loop
                    valid = 0 
                    break
                else:
                    valid = 1
            #if still valid, then we append this number to our result list 
            if valid == 1: 
                result.append(num)
            valid = 0 
        #return result list
        return result
            
                    
                
        