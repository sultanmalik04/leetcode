## Python

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        result = [None]*(n+1)
        result[1] = 1
        result[2] = 2
        for i in range(3,n+1):
            result[i] = result[i-1] + result[i-2]
        return result[n]
```
## Java
```java
public class Solution {
    public int climbStairs(int n) {
        if (n == 1) return 1;
        int[] result = new int[n + 1];
        result[1] = 1;
        result[2] = 2;
        for (int i = 3; i <= n; i++)
            result[i] = result[i - 1] + result[i - 2];
        return result[n];
    }
}
```