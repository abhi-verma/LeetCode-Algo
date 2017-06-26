"""
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6
Example 2:
Input: [1,2,3,4]
Output: 24
"""
import sys
class Solution(object):

    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(nlog(n)). Sorting the nums array takes nlog(n) time.
        Space complexity : O(log(n)). Sorting takes O(logn) space.
        """
        nums.sort()
        
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
    
    
    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(n^3) We need to consider every triplet from numsnums array of length n.
        Space complexity : O(1). Constant extra space is used.
        """
        max_product = nums[0] * nums[1] * nums[2]
        
        for i in range(len(nums)):
          for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
              max_product =  max(max_product, nums[i] * nums[j] * nums[k])
              
        return max_product
    
    def maximumProduct2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time complexity : O(n). Only one iteration over the numsnums array of length nn is required.
        Space complexity : O(1). Constant extra space is used.
        """
        max1 = -sys.maxsize-1
        max2 = -sys.maxsize-1
        max3 = -sys.maxsize-1
        min1 = sys.maxsize
        min2 = sys.maxsize
        
        for i in nums:
          if i <= min1:
            min2 = min1
            min1 = i
          elif i <= min2:
            min2 = i
            
          if i >= max1:
            max3 = max2
            max2 = max1
            max1 = i
          elif i >= max2 and i < max3:
            max3 = max2
            max2 = i
          elif i >= max3:
            max3 = i
        
        return max(min1 * min2 * max1, max1 * max2 * max3)
        
        
print(Solution().maximumProduct([-4, -3, -1, 1, 2, 3]))
print(Solution().maximumProduct1([-4, -3, -1, 1, 2, 3]))
print(Solution().maximumProduct2([-4, -3, -1, 1, 2, 3]))
