class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(nums) - len(nums)*min(nums)
        
a = Solution()
print(a.minMoves([1,2,3]))
