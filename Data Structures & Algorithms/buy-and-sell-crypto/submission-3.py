class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0

        while r < len(prices):
            total = prices[r] - prices[l]
            maxP = max(maxP, total)
            if prices[r] < prices[l]:
                l = r
            
            r += 1
        
        return maxP
            