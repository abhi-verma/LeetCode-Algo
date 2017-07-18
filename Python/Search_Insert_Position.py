"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if target in nums:
          return nums.index(target)
        elif target < nums[0]:
          return 0
        elif target > nums[-1]:
          return len(nums)
        else:
          for i in range(len(nums)-1):
            if target > nums[i] and target < nums[i+1]:
              return i+1
        
        

nums = [1,3,5,6]
a = Solution()
print(a.searchInsert(nums, 2))
