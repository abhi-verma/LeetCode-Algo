"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        Time Complexity: O(N)
        """
        
        if s.count('A') > 1 or s.count('LLL') > 0:
          return False
        
        return True

    def checkRecord1(self, s):
        """
        :type s: str
        :rtype: bool
        Time Complexity: O(N)
        """
        
        count_absent = 0
        
        for chr in s:
          if chr == 'A':
            count_absent += 1
            if count_absent > 1:
              return False
        
        for i in range(0, len(s)-2):
          if s[i] == 'L' and s[i+1] == 'L' and s[i+2] == 'L':
            return False
        
        return True

a = Solution()
print(a.checkRecord("PPALLL"))
print(a.checkRecord1("PPALLL"))
