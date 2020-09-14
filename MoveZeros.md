## Python
```python
# Two Pointer approach
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        lastNonZero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[lastNonZero], nums[i] = nums[i], nums[lastNonZero]
                lastNonZero += 1

## One Liner
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        nums = [nums.append(nums.pop(i)) 
                for i in range(len(nums)-1, -1, -1) 
                if nums[i] == 0]
```