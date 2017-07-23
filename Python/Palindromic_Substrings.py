"""
Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution(object):
    def countSubstrings(self, s):
        def check(s):
            return s == s[::-1]
        cnt = len(s)
        for i in range(len(s)):
            for j in range(i + 2, len(s) + 1):
                if check(s[i:j]):
                    cnt += 1
        return cnt

a = Solution()
print(a.countSubstrings('aaa'))
