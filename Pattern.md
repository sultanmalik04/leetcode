
## Python
```python
n = int(input())
s = n*2 - 1
array = [n]*(s)
j = 0
for i in range(n):
    j += 1
    print(*array)
    for k in range(j,s-j):
        val = n - j
        array[k] = val
for i in range(n-1):
    j -= 1
    val += 1
    for k in range(j,s-j):
        array[k] = val
    print(*array)

# Output:
'''
n = 4
4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4'''
```