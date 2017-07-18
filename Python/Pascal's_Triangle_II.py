"""
Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].
"""

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        """
        pascal = [1] * (rowIndex+1)
        
        for i in range(1,rowIndex+1):
          for j in range(i-1, 0, -1):
            pascal[j] += pascal[j-1]
        
        return pascal 
        
a = Solution()
print(a.getRow(10))
