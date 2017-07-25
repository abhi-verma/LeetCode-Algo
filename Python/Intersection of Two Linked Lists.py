# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA,currB = headA,headB
        
        lenA, lenB = 0, 0
        
        while currA:
          lenA += 1
          currA = currA.next
        
        while currB:
          lenB += 1
          currB = currB.next
          
        currA,currB = headA,headB
        
        if lenA > lenB:
          for _ in range(lenA - lenB):
            currA = currA.next
        else:
          for _ in range(lenB - lenA):
            currB = currB.next
        
        while currA != currB:
          if currA == currB:
            return currA
          currA = currA.next
          currB = currB.next
        
        return currA

class Solution1(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        currA = headA
        currB = headB
        
        d = {}
        
        while currA:
          d[currA.val] = currA
          currA = currA.next
        
        while currB:
          if currB.val in d:
            return currB
          else:
            currB = currB.next
