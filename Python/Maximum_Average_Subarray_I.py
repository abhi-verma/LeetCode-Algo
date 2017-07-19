"""
Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
"""

class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        
        if len(nums) <= k:
            return sum(nums) / float(k)
        
        
        res = sum(nums[0:k])
        cur = res
        for i in range(k, len(nums)):
            cur = cur + nums[i] - nums[i-k]
            if cur > res:
                res = cur
                
        return res/float(k)
    
    def findMaxAverage1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        Time Complexity: O(N)
        Space Complexity: O(N)
        """
        if len(nums) <= k:
          return sum(nums)/float(k)
        
        max_avg = float('-inf')
        
        sums1 = []
        sums1.insert(0, nums[0])
        
        for i in range(1,len(nums)):
          sums1.append(sums1[i-1] + nums[i])
          
        max_avg = sums1[k-1] / float(k)
        
        for i in range(k, len(sums1)):
          max_avg = max(max_avg, (sums1[i] - sums1[i-k]) / float(k))
        
        return max_avg
        
a = Solution()
print(a.findMaxAverage([0,4,0,3,2], 1))
print(a.findMaxAverage1([0,4,0,3,2], 1))
