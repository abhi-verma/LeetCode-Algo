"""
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:
Input: "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        Time complexity : O(n).
        Space complexity : O(n).
        """
        arr = s.split(' ')
        return ' '.join(i[::-1] for i in arr)
        
a = Solution()
print(a.reverseWords("Let's take LeetCode contest"))
