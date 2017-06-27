"""
Given m arrays, and each array is sorted in ascending order. Now you can pick up two integers from two different arrays (each array picks one) and calculate the distance. We define the distance between two integers a and b to be their absolute difference |a-b|. Your task is to find the maximum distance.
Example 1:
Input: 
[[1,2,3],
 [4,5],
 [1,2,3]]
Output: 4
Explanation: 
One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Note:
Each given array will have at least 1 number. There will be at least two non-empty arrays.
The total number of the integers in all the m arrays will be in the range of [2, 10000].
The integers in the m arrays will be in the range of [-10000, 10000].
"""

class Solution(object):
    def maxDistance(self, arrays):
        """
        :type arrays: List[List[int]]
        :rtype: int
        Time complexity : O(n). We traverse over the listlist of length nn once only.
        Space complexity : O(1). Constant extra space is used.
        """
        maxVal = arrays[0][-1]
        minVal = arrays[0][0]
        res = 0
        
        for i in range(1, len(arrays)):
          res = max(res, abs(arrays[i][-1]-minVal), abs(maxVal-arrays[i][0]))
          minVal = min(arrays[i][0], minVal)
          maxVal = max(arrays[i][-1], maxVal)
        
        return res
        
        
print(Solution().maxDistance([[-8,-7,-7,-5,1,1,3,4],[-2],[-10,-10,-7,0,1,3],[2]]))
