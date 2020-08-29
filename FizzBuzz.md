## Python
```python
class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = ['FizzBuzz' if i%3==0 and i%5==0 else 'Fizz' if i%3 == 0 else 'Buzz' if i%5 == 0 else str(i) for i in range(1,n+1)]
        return result
```

## Java
```java
    import java.util.*;

    class Solution {
        public List<String> fizzBuzz(int n) {
            List<String> result = new Vector<String>(n);
            for (int i=1; i <= n; i++){
                if (i%3 == 0 && i%5 == 0)  result.add("FizzBuzz");
                else if (i%3 == 0)  result.add("Fizz");
                else if (i%5 == 0)  result.add("Buzz");
                else result.add(Integer.toString(i));
            }
            return result;
        }
    }
```