"""
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.

You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
"""

class Solution(object):
    def findUnsortedSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(nlogn) Sorting takes nlogn time.
        Space complexity : O(n) We are making copy of original array.
        """
        sorted_nums = sorted(nums)
        start = len(nums)
        end = 0
        
        for i in range(len(nums)):
          if nums[i] != sorted_nums[i]:
            start = min(start, i)
            end = max(end, i)
        
        if end-start >= 0:
          return end-start+1
        else:
          return 0
          
    def findUnsortedSubarray1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(n). Stack of size nn is filled.
        Space complexity : O(n). Stack size grows upto n.
        """
        stack = []
        left = len(nums)
        right = 0
        
        for i in range(len(nums)):
          while(len(stack) != 0 and nums[stack[-1]] > nums[i]):
            left = min(left, stack.pop())
          stack.append(i)
        
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
          while(len(stack) != 0 and nums[stack[-1]] < nums[i]):
            right = max(right, stack.pop())
          stack.append(i)
        
        if right-left >= 0:
          return right-left+1
        else:
          return 0
        
    def findUnsortedSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
          return 0
        
        min_arr = min(nums)
        max_arr = max(nums)
        
        if nums[0] == min_arr and nums[-1] == max_arr:
          return self.findUnsortedSubarray1(nums[1:-1])
        elif nums[0] == min_arr and nums[-1] != max_arr:
          return self.findUnsortedSubarray1(nums[1:])
        elif nums[0] != min_arr and nums[-1] == max_arr:
          return self.findUnsortedSubarray1(nums[:-1])
        else:
          return len(nums)
        
        
a = Solution()
print(a.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
print(a.findUnsortedSubarray1([2, 6, 4, 8, 10, 9, 15]))
print(a.findUnsortedSubarray2([2, 6, 4, 8, 10, 9, 15]))
