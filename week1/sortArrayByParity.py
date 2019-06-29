class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        list1 = []
        list2 = []
        for number in A:
            if number%2 == 0:
                list1.append(number)
            else:
                list2.append(number)
        return list1+list2
        
"""
Thought process:

What we can do is iterate through the array and test each number 

Our test will be number%2 == 0 
if True, our number has no remainder when divided by zero and is thus even. 
Otherwise the number is odd.

We create an even and odd array and add the elements to their respective array during our 
iteration. 

Then it is only a matter of concatenating our even array with our odd array :] 


"""