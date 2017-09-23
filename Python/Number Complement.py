"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        bin_num = "{0:b}".format(num)
        
        list_num = list(bin_num)
        
        for i in range(0, len(list_num)):
          if list_num[i] == '0':
            list_num[i] = '1'
          elif list_num[i] == '1':
            list_num[i] = '0'
        
        comp_num = ''.join(list_num)
        
        return int(comp_num, 2)
          

a = Solution()
print(a.findComplement(1))
