"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""

class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        outList = []
        
        for i in range(1, n+1):
          if i % 3 == 0 and i % 5 == 0:
            outList.append('FizzBuzz')
          elif i % 3 == 0:
            outList.append('Fizz')
          elif i % 5 == 0:
            outList.append('Buzz')
          else:
            outList.append(i)
        
        return outList


a = Solution()
print(a.fizzBuzz(15))
