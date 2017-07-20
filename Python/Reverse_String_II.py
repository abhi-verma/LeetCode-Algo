"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.
Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"
"""


class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        a = ''
        out = ''
        
        for i in range(0, len(s), 2*k):
          a = s[i:i+2*k]
          if len(a) < k:
            out += a[::-1]
          elif len(a) < 2*k and len(a) >= k:
            out += (a[k-1::-1] + a[k:])
          elif len(a) == 2*k:
            out += (a[k-1::-1] + a[k:])
        
        return out
        
a = Solution()
print(a.reverseStr("abcdefg", 2))
