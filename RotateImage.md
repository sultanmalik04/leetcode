## Python
```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        j = 0
        for i in list(zip(*matrix)):
            matrix[j] = list(i)
            j += 1
        print(matrix)
        for i in range(n):
            matrix[i] = matrix[i][::-1]
```