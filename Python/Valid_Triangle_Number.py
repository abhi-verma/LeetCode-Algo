"""
Given an array consists of non-negative integers, your task is to count the number of triplets chosen from the array that can make triangles if we take them as side lengths of a triangle.

Example 1:
Input: [2,2,3,4]
Output: 3
Explanation:
Valid combinations are: 
2,3,4 (using the first 2)
2,3,4 (using the second 2)
2,2,3
Note:
The length of the given array won't exceed 1000.
The integers in the given array are in the range of [0, 1000].
"""

class Solution(object):
           
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(n^2). Loop of k and j will be executed O(n^2) times in total, because, we do not reinitialize the value of k for a new value of j chosen(for the same i). Thus the complexity will be O(n^2+n^2)=O(n^2).
        Space complexity : O(logn). Sorting takes O(logn) space.
        """
        
        count = 0
        nums.sort()
        
        for i in range(len(nums)-2):
          k = i+2
          for j in range(i+1, len(nums)):
            if nums[i] != 0:
              while k < len(nums) and nums[i] + nums[j] > nums[k]:
                k += 1
              count += (k - j - 1)
        return count
      
    def triangleNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(n^3). Three nested loops are there to check every triplet.
        Space complexity : O(1)O(1). Constant space is used.
        """
        
        count = 0
        
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
              if nums[i] + nums[j] > nums[k] and nums[k] + nums[j] > nums[i] and nums[i] + nums[k] > nums[j]:
                count += 1
                
        return count
        
    def triangleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        count = 0
        nums.sort()
        
        for i in range(len(nums)):
          left = 0
          right = i - 1
          while left < right:
            if nums[left] + nums[right] > nums[i]:
              count += right - left
              right -= 1
            else:
              left += 1
                
        return count
        
        
print(Solution().triangleNumber([2,2,3,4]))
print(Solution().triangleNumber1([2,2,3,4]))
print(Solution().triangleNumber2([2,2,3,4]))
