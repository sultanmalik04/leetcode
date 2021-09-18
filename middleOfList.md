## Python
#### Approach 1
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def middleNode(head):
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        i = 0
        while i < l//2: 
            head = head.next
            i += 1
        return head
```

#### Approach 2
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:    
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
```