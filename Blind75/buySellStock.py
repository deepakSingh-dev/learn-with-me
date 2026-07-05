class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price                 # best day to buy so far
            else:
                profit = price - min_price        # sell today
                if profit > max_profit:
                    max_profit = profit

        return max_profit