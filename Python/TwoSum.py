"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1]
"""

class Solution(object):
    def twoSum1(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        
        d = {}
        
        for i in range(len(nums)):
            if (target-nums[i]) in d:
                return [nums.index(target-nums[i]), i]
            else:
                d[nums[i]] = i
        
        return 'No solution for the arguments passed'
   
    def twoSum2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        
        aim = 0
        k = 0
        
        for i in nums:
            
            aim = target - i
            k = k + 1
            
            if aim in nums[k:]:
                return [nums.index(i), nums.index(aim)]
        
        return 'No solution for the arguments passed'


nums = [2, 7, 11, 15]
target = 26
print(Solution().twoSum1(nums, target))
print(Solution().twoSum2(nums, target))
