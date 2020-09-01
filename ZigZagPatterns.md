```python
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        result = ''
        factor = 2*(numRows-1)

        for i in range(numRows):
            for j in range(0, len(s), factor):
                if i+j < len(s):
                    result += s[i+j]
                    if i != 0 and i != numRows-1 and j+factor-i < len(s):
                        result += s[j+factor-i]
        return result
```