class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
          return False
        
        sum = 0
        num = x
        
        while num > 9:
          sum *= 10
          sum += (num % 10) * 10
          num = num // 10
        
        return sum + num == x
        
a = Solution()
print(a.isPalindrome(12345))
