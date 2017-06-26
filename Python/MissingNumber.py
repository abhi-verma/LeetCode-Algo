class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        
        if nums[0] != 0:
          return 0
        
        for i in range(len(nums)-1):
          if nums[i+1] == nums[i] + 1:
            continue
          else:
            return nums[i]+1
        
        return nums[-1] + 1
        
    def missingNumber1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        sum = 0
        
        for i in nums:
          sum += i
        
        return int((len(nums)*(len(nums)+1))/2 - sum)

print(Solution().missingNumber([2,0,1]))
print(Solution().missingNumber([2,0,1]))
