## Python
```python
class Solution(object):
    def myAtoi(self, str):
        sign, result = 1, 0
        i = 0
        while i < len(str) and str[i] == ' ':
            i += 1
        if i >= len(str):
            return 0
        if i < len(str) and str[i] == '-' or str[i] == '+':
            if str[i] == '-':
                sign = -1 
                i += 1
            else:
                i += 1
        if i < len(str) and not str[i].isnumeric():
            return 0
        while i < len(str) and str[i].isnumeric():
            result = result * 10 + int(str[i])
            i += 1
        if result >= 2**31 and sign == -1:
            return sign*2147483648
        elif result > 2**31 - 1 and sign == 1 :
            return sign*2147483647
        return sign*result
```
