## Python
```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        mid = temp = head
        while temp and temp.next:
            mid = mid.next
            temp = temp.next.next
            
        prev = None
        while mid:
            cur = mid
            mid = mid.next
            cur.next = prev
            prev = cur
            
        while prev:
            if head.val != prev.val:
                return False
            head, prev = head.next, prev.next
        
        return True
```

## Java
```java
class Solution {
    public boolean isPalindrome(ListNode head) {
        ListNode temp, mid;
        temp = mid = head;
        while (temp != null && temp.next != null){
            mid = mid.next;
            temp = temp.next.next;
        }
        
        ListNode prev = null;
        while (mid != null){
            ListNode cur = mid;
            mid = mid.next;
            cur.next = prev;
            prev = cur;
        }
        
        while (prev != null){
            if (prev.val != head.val){
                return false;
            }
            prev = prev.next;
            head = head.next;
        }
        return true;
    }
}
```