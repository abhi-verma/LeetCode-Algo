class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        
        for i in range(len(nums)-1):
          if nums[i] == nums[i+1]:
            return True
        
        return False
        
          
a = Solution()
print(a.containsDuplicate([3,5,7,1,3,7]))
