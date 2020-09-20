>return fibbonacci(N)
## Python
```python
class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        f, s = 0, 1
        result = f + s
        for i in range(2,N+1):
            result = f + s
            f, s = s, result
        return result
```