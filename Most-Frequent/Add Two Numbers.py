'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807

Time complexity : O(max(m,n)). Assume that m and n represents the length of l1 and l2 respectively, the algorithm iterates at most max(m, n) times.
Space complexity : O(max(m,n)). The length of the new list is at most max(m,n) + 1.
Link: https://leetcode.com/problems/add-two-numbers/description/
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        curr = dummy
        carry = 0
        
        while l1 or l2:
          val = carry
          if l1:
            val += l1.val
            l1 = l1.next
          if l2:
            val += l2.val
            l2 = l2.next
          carry, val = divmod(val, 10)
          
          curr.next = ListNode(val)
          curr = curr.next
        
        if carry == 1:
          curr.next = ListNode(carry)
        
        return dummy.next      

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print(result.val, result.next.val, result.next.next.val)
