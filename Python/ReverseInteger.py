"""
Reverse digits of an integer.

Example1: x = 123, return 321
Example2: x = -123, return -321

click to show spoilers.

Have you thought about this?
Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!

If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.

Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?

For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution(object):
    def reverse1(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
          x = int(str(x)[::-1][-1] + str(x)[::-1][:-1])
        else:
          x = int(str(x)[::-1])
          
        if abs(x) > 0x7FFFFFFF:
          return 0
        else:
          return x
    
    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        result = 0
        
        pos_int = abs(x)
        
        while pos_int:
          result = result * 10 + pos_int % 10
          pos_int = pos_int // 10
        
        if result <= 0x7fffffff:
          if x < 0:
            return result * -1
          else:
            return result
        else:
          return 0
        
print(Solution().reverse1(1234))
print(Solution().reverse2(1234))
