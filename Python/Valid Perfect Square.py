"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:

Input: 16
Returns: True
Example 2:

Input: 14
Returns: False
"""

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        left = 1
        right = num//2
        mid = (left + right)//2
        
        if left * left == num or right * right == num:
          return True
        
        while left != mid:
          if mid * mid == num:
            return True
          elif mid * mid < num:
            left = mid
            mid = (left + right)//2
          else:
            right = mid
            mid = (left + right)//2
        
        return False

a = Solution()
print(a.isPerfectSquare(4))
