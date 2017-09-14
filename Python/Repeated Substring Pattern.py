"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example 1:
Input: "abab"

Output: True

Explanation: It's the substring "ab" twice.
Example 2:
Input: "aba"

Output: False
Example 3:
Input: "abcabcabcabc"

Output: True

Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)
"""

class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ss = (s + s)[1:-1]
        return ss.find(s) != -1
    
    def repeatedSubstringPattern1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if s[0]*len(s) == s and len(s) != 1:
          return True
        
        for i in range(len(s)//2, 1, -1):
          if len(s)%i == 0:
            if s[:i]*(len(s)//i) == s:
              return True
        
        return False

a = Solution()
print(a.repeatedSubstringPattern('aaa'))
print(a.repeatedSubstringPattern1('aaa'))
