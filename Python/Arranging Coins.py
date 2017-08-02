class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(0.5 * ((8 * n + 1)**0.5 - 1))
          
        
a = Solution()
print(a.arrangeCoins(3))
