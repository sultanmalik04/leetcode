## Python
```python
class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        i = len(s) - 1
        prev = 0
        while i >= 0:
            if dic[s[i]] >= prev:
                result += dic[s[i]] 
            else:
                result -= dic[s[i]]
            prev = dic[s[i]]
            i -= 1
        return result
```