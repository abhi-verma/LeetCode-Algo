class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = float('inf')
        
        for i in range(len(prices)):
          if prices[i] < min_price:
            min_price = prices[i]
          elif prices[i] - min_price > max_profit:
            max_profit = prices[i] - min_price
        return max_profit
            
        
          
a = Solution()
print(a.maxProfit([7, 1, 5, 3, 6, 4]))
