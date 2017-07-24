class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        d = {}
        st = []
        ans = []
        
        for i in nums:
          while st and st[-1] < i:
            d[st.pop()] = i
          st.append(i)
        
        for j in findNums:
          ans.append(d.get(j, -1))
        
        return ans

findNums = [4,1,2]
nums = [1,3,4,2]
a = Solution()
print(a.nextGreaterElement(findNums, nums))
