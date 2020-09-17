#### Problem Statement
>Write a program to find the node at which the intersection of two singly linked lists begins

## Python
```python
class Solution:
    def length(self,head):
        l = 0
        while head:
            l += 1
            head = head.next
        return l

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        l1 = self.length(headA)
        l2 = self.length(headB)
        if l1 > l2:
            for i in range(l1 - l2):
                headA = headA.next
        else:
            for i in range(l2 - l1):
                headB = headB.next
        while headA and headB:
            if headA == headB:
                return headA
            headA, headB = headA.next, headB.next
```