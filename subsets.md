## Python
#### 1st method
```python
from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []            
        for i in range(len(nums)+1):
            tmp = [list(t) for t in combinations(nums, i)]
            for x in tmp:
                ret.append(x)
        return ret
```
#### 2nd method
```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = [[]]
        for num in nums:
            ret += [i + [num] for i in ret]
        return ret
```