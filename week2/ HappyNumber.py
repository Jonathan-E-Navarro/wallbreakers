class Solution:
    def isHappy(self, n: int) -> bool:
        def find_happy(n,attempts):
            # print("n: ",n)
            attempts+=1
            if n == 1:
                return True
            elif attempts == 10:
                return False
            else:
                sum = 0 
                digits = str(n)
                for digit in digits:
                    # print(digit)
                    sum+=int(digit)**2
                # print(sum)
                return find_happy(sum,attempts)
            
        return find_happy(n,0)