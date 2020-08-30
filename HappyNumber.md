## Python
```python
    class Solution:
        def isHappy(self, n: int) -> bool:
            k = 0
            while n != 1 and k < 6:
                n = sum([int(i)**2 for i in str(n)])
                k += 1
            return True if n == 1 else False
```