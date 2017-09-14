"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u']
        i = 0
        j = len(s)-1
        s = list(s)
        
        while i < j:
          if s[i].lower() not in vowels and s[j].lower() not in vowels:
            i += 1
            j -= 1
          elif s[i].lower() not in vowels and s[j].lower() in vowels:
            i += 1
          elif s[i].lower() in vowels and s[j].lower() not in vowels:
            j -= 1
          else:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i += 1
            j -= 1
        
        return ''.join(s)

a = Solution()
print(a.reverseVowels('aA'))
