"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Space Complexity : O(1). Only constant space is used.
        Time Complexity: O(n). However, the total number of operations are still sub-optimal. The total operations (array writes) that code does is nn (Total number of elements).
        """
        index = 0
        
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[index] = nums[i]
            index +=1
        
        for i in range(index, len(nums)):
          nums[i] = 0
        
        return nums
    
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        Space Complexity : O(1). Only constant space is used.
        Time Complexity: O(n) However, the total number of operations are optimal. The total operations (array writes) that code does is Number of non-0 elements.
        """
        index = 0
        
        for i in range(len(nums)):
          if nums[i] != 0:
            nums[index], nums[i] = nums[i], nums[index]
            index += 1
        
        return nums

print(Solution().moveZeroes([0,0,1,2,0]))
print(Solution().moveZeroes1([0,0,1,2,0]))
