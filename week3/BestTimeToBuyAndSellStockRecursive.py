import sys
class Solution(object):
    def __init__(self):
        self.max = 0 
        self.memo = dict()
        self.min_price = 0 
        
    def profit(self,i,length,prices):
        self.memo[i] = max(self.memo[i - 1], prices[i] - self.min_price)
        self.min_price = min(self.min_price, prices[i])
        if i == (length-1):
            return 
        
        self.profit(i+1,length,prices)
            
    
    def maxProfit(self, prices):
        if len(prices) in [0,1]:
            return 0
        self.memo[0] = 0
        
        min_price = prices[0]
        self.min_price = prices[0]
        
        self.profit(1,len(prices),prices)
        return self.memo[len(prices)-1]






'''
greedy recursive approach, works excepts times out on large inputs 
[4,7,3,6,3,6,32,2,4,1,5,3,6,4]
'''
# import sys
# class Solution(object):
#     def __init__(self):
#         self.max = 0 
#         self.memo = dict()
#         self.reached = False
    
#     def profit(self,buy,sell,prices,length):
#         #if buy on last day or if sell over last day 
#         if buy > length or sell >= length :
#             return 
    
#         #if profit can be earned 
#         elif sell > buy:
#             # print("buy: ",prices[buy],"sell: ",prices[sell])
#             profit = prices[sell]-prices[buy]
#             if profit > self.max:
#                 self.max = profit 
#                 # print("max: ",self.max)
#             #if we hit the end of the array, we have found max profit 
#             if sell == length-1:
#                 self.reached = True
#             return
                
#         # print("buy: ",prices[buy],"sell: ",prices[sell])
#         next_sell = sell
        
        
#         while next_sell < length:
#             if prices[buy] < prices[next_sell]:
#                 # print("current: ",prices[buy],'try:',prices[next_sell])
#                 self.profit(buy,next_sell,prices,length)
                
#             elif prices[buy] > prices[next_sell]:
#                 # print("current: ",prices[buy],'move up') 
#                 self.profit(next_sell,next_sell,prices,length)
            
#             #if max profit found, break out of loop 
#             if self.reached:
#                 return
#             next_sell+=1 
            
#         return
            
    
#     def maxProfit(self, prices):
#         length = len(prices) 
#         if length== 0 :
#             return 0 
        
#         self.profit(0,0,prices,length)
#         return self.max
        
        
        
        
        
        
        
'''
another way that still also times out unfortunately 
'''

# import sys
# class Solution(object):
#     def __init__(self):
#         self.max = 0 
#         self.memo = set()
#         self.reached = False
    
#     def profit(self,buy,sell,prices,length):
#         #if profit can be earned 
#         if prices[sell] > prices[buy]:
#             # print("buy: ",prices[buy],"sell: ",prices[sell])
#             profit = prices[sell]-prices[buy]
#             if profit > self.max:
#                 self.max = profit 
#                 # print("new max: ",self.max)
#             #if we hit the end of the array, we have found max profit 
#             if sell == length-1:
#                 self.reached = True
#             return
        
#         # print("buy: ",prices[buy],"sell: ",prices[sell])
#         if buy in self.memo:
#             return
                
            
#         if sell+1 >= length:
#             return
        
        
#         if max(prices[buy:]) > prices[buy]:
#             # print("yaw")
#             self.memo.add(buy)
#             # print(prices[buy:])
#             self.profit(buy,prices.index(max(prices[buy:])),prices,length)
            
#         # print("yeet")
#         self.profit(buy+1,sell+1,prices,length)
        
        
    
#     def maxProfit(self, prices):
#         length = len(prices) 
#         if length== 0 :
#             return 0 
#         s = sorted(prices,reverse = True)
#         if prices == s:
#             return 0

        
#         self.profit(0,0,prices,length)
#         return self.max
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

                
         
        
        
        
        
        
        
        
        
        
        
        
        

                
        