class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        max_ones = 0
        
        for i in nums:
          if i == 1:
            count += 1
            if count > max_ones:
              max_ones = count
          else:
            count = 0
        
        return max_ones
        
          
a = Solution()
print(a.findMaxConsecutiveOnes([1,1,0,1,1,1]))
