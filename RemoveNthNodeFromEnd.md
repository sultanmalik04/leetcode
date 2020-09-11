## Python
```python
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        
        temp = prev = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        
        # when we have to remove first element
        if n == l:    
            return head.next
        
        position = l - n 
        temp = head
        while position:  # iterate to the position of element to be deleted
            prev = temp
            temp = temp.next
            position -= 1
        
        if temp.next:   
            prev.next = temp.next
        else:
            prev.next = None  # Else executes only when we have to remove last element
        
        return head
```