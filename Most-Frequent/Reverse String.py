'''
Write a function that takes a string as input and returns the string reversed.
Example:
Given s = "hello", return "olleh".

Link: https://leetcode.com/problems/reverse-string/description/

'''
class Solution(object):
    def reverseString1(self, s):
        """
        :type s: str
        :rtype: str
        Time complexity : O(N)
        Space complexity : O(N)
        """

        return s[::-1]
    
    def reverseString2(self, s):
        """
        :type s: str
        :rtype: str
        Time complexity : O(N)
        Space complexity : O(N)
        """

        out = ''
        
        for ele in s:
          out = ele + out
        
        return out

a = Solution()
print(a.reverseString1('Hello'))
print(a.reverseString2('Hello'))
