class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if not ops: return m * n
        
        x = [op[0] for op in ops]
        y = [op[1] for op in ops]
        
        m_min = min(m, min(x))
        n_min = min(n, min(y))
        
        return m_min * n_min
        
        
a = Solution()
print(a.maxCount(3,3, [[2,2],[3,3]]))Range Addition II
