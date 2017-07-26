# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # find mid point
        slow = head
        fast = head.next
        while fast and fast.next:
          slow = slow.next
          fast = fast.next.next
        
        # reverse the second half
        cur = slow.next
        slow.next = None
        pre = None
        
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        
        # compare values from two halves
        tail = pre
        while head and tail:
            if head.val != tail.val:
                return False
            head = head.next
            tail = tail.next
        
        return True
    
    def printList(self, head):
        """
        :type head: ListNode
        Prints the linked list
        """
        if not head:
          print('Empty List')
        else:
          while head:
            print(str(head.val), end= " ")
            head = head.next
          print()
            
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(2)
n5 = ListNode(1)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5



a = Solution()
print('List before call:')
a.printList(n1)

print()
print('Palindrome?: '+ str(a.isPalindrome(n1)))
