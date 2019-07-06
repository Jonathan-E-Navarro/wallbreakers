class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        candy_set = set(candies)
        #there are x candies
        #there are y types of candies 
        #if the number of the types of candies >= (number of candies/2), then the girl can gain n/2 
        #else, she can only gain the amount of types that their are 
        
        candy_amount=len(candies)        
        type_amount=len(set(candies))    
        
        if type_amount>=candy_amount/2:
            return int(candy_amount/2)
        else:
            return type_amount

