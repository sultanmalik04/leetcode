#### Problem Statement
>Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.


## Python
1st method: insertion sort
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        for k in range(1,len(nums)):
            x = nums[k]
            i = k - 1 
            while i >= 0 and nums[i] > x:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = x
```
2nd method
```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # we can maintain 2 pointers left and right
        l, r = 0, len(nums)-1
        i = 0
        while i <= r:
            # if 0 appears put it to left side
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            # if 2 appears put it to right side
            elif nums[i] == 2:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            # if 1 appears don't change it's position
            else:
                i += 1
```