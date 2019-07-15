import sys
class Solution(object):
    def __init__(self):
        "memoization table, use hash table instead of list for lookup speed"
        self.memo = dict()
    
    def maxProfit(self, prices):
        '''
        O(n) one pass version
        we keep track of the lowest price seen so far, 
        and keep updating max_profit as we go along.
        instead of creating a recursive function that memoizes the results, 
        we keep track of the max profit and min price
        # max_profit = 0 
        # min_price = sys.maxsize
        # for i in range(len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     elif prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price
        # return max_profit
        '''

        #DP VERSION
        if len(prices)==0:
            return 0
        '''we want to buy cheap and sell BIG'''
        '''initalize profit table '''
        self.memo[0] = 0 
        '''first min price is first price'''
        min_price = prices[0]

        '''iterate through prices from second day on, since buying and selling on day one will net zero '''
        for i in range(1,len(prices)):
            '''max profit at point i is max(having sold before today or selling today) '''
            self.memo[i] = max(self.memo[i - 1], prices[i] - min_price)
            '''always track smallest price we are able to buy '''
            min_price = min(min_price, prices[i])

        '''last entry will be max profit when taking all days into account '''
        return self.memo[len(prices)-1]

                    
                
        