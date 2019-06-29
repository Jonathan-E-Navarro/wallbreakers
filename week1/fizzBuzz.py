class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for num in range(1,n+1):
            if num%3 == 0 and num%5 == 0:
                result.append("FizzBuzz")
            elif num%3 == 0:
                result.append("Fizz")
            elif num%5 == 0:
                result.append("Buzz")
            else:
                result.append(str(num))
        return result

"""
Thought process:
First we create an empty list that will carry our results, then we acknowledge that
if a number x is divisible by a number y, then x%y should equal 0


This knowledge makes this problem easy for us in that all we have to do is iterate
through the range of numbers and run it through a series of if and else if statements that 
test whether that number is divisible by 3, by 5 , both or none and handle appending the 
appropriate output to our result list :] 
"""