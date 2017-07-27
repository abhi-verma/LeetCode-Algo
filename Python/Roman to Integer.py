class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        
        num = 0
        
        for i in range(len(s)):
          if s[i] == 'I' and i < len(s)-1 and (s[i+1] == 'X' or s[i+1] == 'V'):
            num += -1
          elif s[i] == 'X' and i < len(s)-1 and (s[i+1] == 'L' or s[i+1] == 'C'):
            num += -10
          elif s[i] == 'C' and i < len(s)-1 and (s[i+1] == 'D' or s[i+1] == 'M'):
            num += -100
          else:
            num += d[s[i]]
          
        return num
        
a = Solution()
print(a.romanToInt('MCMXCVI'))
