class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        else:
            tmp = bin(n)[2:]
            if tmp[0] == '1' and tmp.count('1') == 1:
                return True
            else:
                return False
    
    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        else:
            if n & (n-1) == 0:
              return True
        
        return False
    
    def isPowerOfTwo2(self, n):
        """
        :type n: int
        :rtype: bool
        """
        exp = 0
        ans = 1
        while ans < n:
          ans *= 2
          exp += 1
        if ans == n:
          return True  
        else:
          return False

        
a = Solution()
print(a.isPowerOfTwo(32))
print(a.isPowerOfTwo1(32))
print(a.isPowerOfTwo2(32))
