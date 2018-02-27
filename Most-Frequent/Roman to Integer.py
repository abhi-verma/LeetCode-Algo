'''
Given a roman numeral, convert it to an integer.
Input is guaranteed to be within the range from 1 to 3999.

Time complexity : O(n), where n is the length of the string.
Space complexity : O(1).

Hint:
* If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
* If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
* If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900

Link: https://leetcode.com/problems/roman-to-integer/description/

'''
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        d = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
        
        num = 0
        cnt = 0
      
        while cnt < len(s):
          if cnt != len(s)-1 and d[s[cnt]] < d[s[cnt+1]]:
            num += (d[s[cnt+1]] - d[s[cnt]])
            cnt += 2
          else:
            num += d[s[cnt]]
            cnt += 1
        
        return num

a = Solution()
print(a.romanToInt('MCMXCVI'))
