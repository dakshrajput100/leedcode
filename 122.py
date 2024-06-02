#case1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxx += prices[i] - prices[i-1]
        return maxx



#case2 using 2 pointer
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxx = 0
        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxx +=profit
                l = r

            else:
                l = r
            r +=1
        return maxx           
