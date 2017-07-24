class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        
        open_brackets = ['[', '(', '{']
        close_brackets = [']', ')', '}']
        
        for ele in s:
          if ele in open_brackets:
            stack.append(ele)
          else:
            if not stack:
              return False
            x = stack.pop()
            if close_brackets.index(ele) != open_brackets.index(x):
              return False
        
        return len(stack) == 0
        
        
s = '[]}'
a = Solution()
print(a.isValid(s))
