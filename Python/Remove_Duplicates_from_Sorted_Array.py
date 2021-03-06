"""
Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the new length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if len(nums) == 0:
          return 0
          
        tail = 0
        
        for j in range(1, len(nums)):
          if nums[j] != nums[tail]:
            tail += 1
            nums[tail] = nums[j]
        
        return tail + 1
            
            
print(Solution().removeDuplicates([1,1,1,1,2]))
