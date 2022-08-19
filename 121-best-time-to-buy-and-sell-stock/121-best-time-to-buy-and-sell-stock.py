class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #sliding window technique, using two pointers
        l,r = 0, 1
        maxProfit = 0
        
        while r< len(prices):
            #only calculate profits
            if(prices[l]<prices[r]):
                p = prices[r] - prices[l]
                maxProfit = max(p,maxProfit)
            else:
                l = r
            r+=1
        return maxProfit