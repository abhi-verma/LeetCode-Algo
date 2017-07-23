"""
You are given n pairs of numbers. In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed. You needn't use up all the given pairs. You can select pairs in any order.

Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
"""

class Solution(object):
    def findLongestChain(self, pairs):
              
        pairs.sort(key = lambda x: x[1])
        
        cnt = 1
        end = pairs[0][1]
        
        for k in pairs[1:]:
          if k[0] > end:
            cnt += 1
            end = k[1]
        
        return cnt


a = Solution()
print(a.findLongestChain([[1,2],[3,4], [5,6]]))
