# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        currNode = head
        prevNode = None
        nextNode = None
        
        while currNode:
          nextNode = currNode.next
          currNode.next = prevNode
          prevNode = currNode
          currNode = nextNode
        
        return prevNode
        
    
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
n4 = ListNode(4)
n5 = ListNode(5)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5



a = Solution()
print('List before call:')
a.printList(n1)

head = a.reverseList(n1)
print()
print('List after call:')
a.printList(head)
