""""
Given a List of words, return the words that can be typed using letters of alphabet on only one row's of American keyboard like the image below.

Example 1:
Input: ["Hello", "Alaska", "Dad", "Peace"]
Output: ["Alaska", "Dad"]
"""
class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        s1 = set("qwertyuiop")
        s2 = set("asdfghjkl")
        s3 = set("zxcvbnm")
        res = []
        
        for word in words:
            s = set(word.lower())
            if s1 & s == s:
                res.append(word)
            elif s2 & s == s:
                res.append(word)
            elif s3 & s == s:
                res.append(word)
        return res
        
a = Solution()
print(a.findWords(["qz","wq","asdddafadsfa","adfadfadfdassfawde"]))
