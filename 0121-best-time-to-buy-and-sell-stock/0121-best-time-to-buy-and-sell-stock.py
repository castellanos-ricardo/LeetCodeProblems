class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0,1
        maxProfit = 0
        
        while right<len(prices):
            #check if there is profit
            if (prices[left] < prices[right]):
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            
            right = right + 1
        
        return maxProfit
                
            