## Python
```python
def maximumPower(s):
    # Write your code here
    result = 0
    for i in range(len(s)):
        b_int = int(s[len(s)-i:] + s[:len(s)-i], 2)
        j = 0
        while b_int % 2**j == 0:
            result = max(result, j)
            j += 1
    return result
s = input()
maximumPower(s)
```