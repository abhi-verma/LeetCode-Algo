"""
Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        
        i = -1
        while digits[i] + 1 == 10:
          if i == -len(digits):
            digits[i] = 0
            digits.insert(0, 1)
            return digits
          elif digits[i] == 9:
            digits[i] = 0
          else:
            digits[i] += 1
            return digits
          i -= 1
          
        digits[i] += 1
          
        return digits
        
a = Solution()
print(a.plusOne([1,0,0,0,0]))
