## Python
#### 1st method
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        
        start = count = 0
        while count < n:
            cur, prev = start, nums[start]
            while True:
                next_index = (cur + k)%n
                nums[next_index], prev = prev, nums[next_index]
                cur = next_index
                count += 1
                if start == cur:
                    break
            start += 1
```
#### 2nd method
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        nums[:] = nums[::-1]
        nums[:] = nums[:k][::-1] + nums[k:][::-1]
```