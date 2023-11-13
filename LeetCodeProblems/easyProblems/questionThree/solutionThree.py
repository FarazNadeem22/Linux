class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = max(prices)
        sellPrice = 0
        for i in range(0, len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]
            else:
                potentialProfit = prices[i] - buyPrice
                if potentialProfit > maxProfit:
                    maxProfit = potentialProfit
        return maxProfit