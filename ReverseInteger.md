## Python
```python
class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            sign = -1
            x = sign*x
        else:
            sign = 1
        while x > 0:
            rev = rev * 10 + x % 10
            x //= 10
        if rev > 2**31:
            rev = 0
        return rev*sign
```
