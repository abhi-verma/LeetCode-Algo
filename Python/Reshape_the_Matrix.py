"""
In MATLAB, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the row number and column number of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        Time complexity : O(m*n). We traverse the entire matrix of size m∗n once only. Here, m and n refers to the number of rows and columns in the given matrix.
        Space complexity : O(m*n). The resultant matrix of size m∗n is used.
        """
        mat_mul = len(nums) * len(nums[0])
        
        col = c
        row = 0
        
        new_matrix = [[]]
        
        if r * c != mat_mul:
          return nums
        else:
          for i in range(len(nums)):
            for j in range(len(nums[i])):
              if col != 0:
                new_matrix[row].append(nums[i][j])
                col -= 1
                if col == 0 and row != r-1:
                  new_matrix.append([])
                  col = c
                  row += 1
          return new_matrix
        
        
nums = [[1,2],[3,4]]
r = 1
c = 4
a = Solution()
print(a.matrixReshape(nums, r, c))
