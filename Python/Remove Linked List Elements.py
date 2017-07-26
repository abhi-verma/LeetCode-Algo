# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        curr = head
        prev = curr
        
        while curr:
          if curr.val == val:
            if head.val == val:
              head = head.next
            prev.next = curr.next
            curr = curr.next
            
          else:
            prev = curr
            curr = curr.next
        
        return head
    
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
n3 = ListNode(6)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(6)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7



a = Solution()
print('List before call:')
a.printList(n1)

head = a.removeElements(n1,6)
print()
print('List after call:')
a.printList(head)
