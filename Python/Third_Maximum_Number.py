"""
Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(N)
        """
        max1 = float('-inf')
        max2 = float('-inf')
        max3 = float('-inf')
        
        for i in range(len(nums)):
          if nums[i] > max1:
            max3 = max2
            max2 = max1
            max1 = nums[i]
          elif max2 < nums[i] < max1:
            max3 = max2
            max2 = nums[i]
          elif max3 < nums[i] < max2:
            max3 = nums[i]
          
        if max3 == float('-inf'):
          return max(nums)
        else:
          return max3
        
a = Solution()
print(a.thirdMax([2,2,3,1]))
