#### Problem Statement
>Reverse a singly linked list.

## Python
```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        ret = ListNode()
        while head:
            if not ret:
                newNode = ListNode(head.val)
                ret.next = newNode
            else:
                newNode = ListNode(head.val)
                newNode.next = ret.next
                ret.next = newNode
            head = head.next
        return ret.next
```